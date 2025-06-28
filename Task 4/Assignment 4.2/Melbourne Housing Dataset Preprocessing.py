import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, MinMaxScaler, RobustScaler, PowerTransformer
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings("ignore")

# Load Dataset
df = pd.read_csv('Melbourne_housing_FULL.csv')  # Replace with your path

### ------------------- PART 1: HANDLING MISSING DATA ------------------- ###
# 1. Check for nulls
print(df.isnull().sum())

# 2. Visualize missing values
sns.heatmap(df.isnull(), cbar=False)
plt.title("Missing Values Heatmap")
plt.show()

# 3. Drop rows where 'Car' is null
df = df.dropna(subset=['Car'])

# 4. Fill 'Car' with median
df['Car'].fillna(df['Car'].median(), inplace=True)

# 5. Fill 'BuildingArea' with mean
df['BuildingArea'].fillna(df['BuildingArea'].mean(), inplace=True)

# 6. Fill 'YearBuilt' with most frequent value
df['YearBuilt'].fillna(df['YearBuilt'].mode()[0], inplace=True)

# 7. Drop 'CouncilArea'
df.drop(columns=['CouncilArea'], inplace=True)

# 8. Fill remaining nulls with their column means (for numeric only)
for col in df.select_dtypes(include=[np.number]).columns:
    df[col].fillna(df[col].mean(), inplace=True)

# 9. Show rows with more than 2 nulls
print(df[df.isnull().sum(axis=1) > 2])

# 10. Replace missing in 'BuildingArea' with 0 (already handled)

# 11. Create new column if 'BuildingArea' was missing (binary indicator)
df['BuildingArea_missing'] = df['BuildingArea'].isnull().astype(int)

# 12. Replace 'Car' with random int between 1 and 4
df['Car'] = df['Car'].apply(lambda x: np.random.randint(1, 5) if pd.isnull(x) else x)

# 13. Use KNNImputer for numeric missing values
numeric_cols = df.select_dtypes(include=[np.number]).columns
imputer = KNNImputer(n_neighbors=3)
df[numeric_cols] = imputer.fit_transform(df[numeric_cols])

# 14. Create summary of missing values
summary = df.isnull().sum()
summary_percent = (df.isnull().sum() / len(df)) * 100
missing_summary = pd.DataFrame({'Missing Values': summary, 'Percent': summary_percent})
print(missing_summary)

# 15. Save cleaned data
df.to_csv('cleaned_melbourne.csv', index=False)

### ------------------- PART 2: ENCODING CATEGORICAL VARIABLES ------------------- ###
# 16. Identify object columns
cat_cols = df.select_dtypes(include='object').columns.tolist()

# 17. LabelEncode 'Type'
le = LabelEncoder()
df['Type'] = le.fit_transform(df['Type'])

# 18. LabelEncode 'Method' and 'SellerG'
df['Method'] = le.fit_transform(df['Method'])
df['SellerG'] = le.fit_transform(df['SellerG'])

# 19. OneHotEncode 'Regionname'
df = pd.get_dummies(df, columns=['Regionname'])

# 20. Get dummies for all object types
df = pd.get_dummies(df, drop_first=True)

# 21. Drop original categorical cols (already done above)

# 22. Extract 'year' from 'Date'
df['Year'] = pd.to_datetime(df['Date']).dt.year
df.drop(columns=['Date'], inplace=True)

# 23. Map 'Type'
df['Type'] = df['Type'].map({0: 'h', 1: 'u', 2: 't'}).fillna('u')

# 24. Use ColumnTransformer (handled later in pipeline)

# 25. Convert 'CouncilArea' to category (already dropped)

### ------------------- PART 3: FEATURE SCALING ------------------- ###
# 31. Numerical features
num_cols = df.select_dtypes(include=[np.number]).columns.tolist()

# 32. StandardScaler
scaler = StandardScaler()
df[['Distance', 'Landsize', 'BuildingArea']] = scaler.fit_transform(df[['Distance', 'Landsize', 'BuildingArea']])

# 33. MinMaxScaler
mms = MinMaxScaler()
df[['Price', 'Rooms']] = mms.fit_transform(df[['Price', 'Rooms']])

# 34. Distribution comparison (optional plot)
df[['Price', 'Rooms']].hist(bins=20)
plt.suptitle("Scaled Price and Rooms")
plt.show()

# 35. RobustScaler
rs = RobustScaler()
df[['Landsize']] = rs.fit_transform(df[['Landsize']])

# 36. ColumnTransformer (see pipeline below)

# 37. Save scaled data
df.to_csv("scaled_data.csv", index=False)

# 38. PowerTransformer
pt = PowerTransformer()
df[['Lattitude', 'Longtitude']] = pt.fit_transform(df[['Lattitude', 'Longtitude']])

# 39. Histogram of scaled features
df[['Distance', 'BuildingArea', 'Rooms']].hist(bins=20)
plt.show()

# 40. Function to apply scaler
def apply_scaler(df, columns, scaler):
    df[columns] = scaler.fit_transform(df[columns])
    return df

### ------------------- PART 4: SPLITTING DATA ------------------- ###
# 41. Features/Target
X = df.drop('Price', axis=1)
y = df['Price']

# 42. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 43. Stratified split (on a real category like 'Regionname' — already encoded)

# 44. Print shapes
print("Train:", X_train.shape, "Test:", X_test.shape)

# 45. Use random_state in split (already done)

# 46. Plot price distribution
sns.histplot(y_train, color="blue", label="Train", kde=True)
sns.histplot(y_test, color="orange", label="Test", kde=True)
plt.legend()
plt.title("Price Distribution")
plt.show()

# 47. Preprocessing pipeline
numeric_features = X.select_dtypes(include=[np.number]).columns
preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), numeric_features)
])
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# 48. Train Linear Regression
pipeline.fit(X_train, y_train)
score = pipeline.score(X_test, y_test)
print("Model R² Score:", score)

# 49. Save train/test
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

# 50. Reusable split function
def split_data(df, target, test_size=0.2):
    X = df.drop(target, axis=1)
    y = df[target]
    return train_test_split(X, y, test_size=test_size, random_state=42)

