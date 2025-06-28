# Simulate DataFrame with a 'Revenue' column for the example
import pandas as pd


data = {'Product': ['A', 'B', 'C'], 'Revenue': [100000, 250000, 175000]}
df_tax = pd.DataFrame(data)

# Add a new column for 5% tax
df_tax['Sales_Tax_5%'] = df_tax['Revenue'] * 0.05
print("\nDataFrame with Sales Tax:\n", df_tax)
