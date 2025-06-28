# Simulated employee salary data
import pandas as pd


data_salary = {
    'Employee': ['John', 'Alice', 'Bob', 'Emma'],
    'Annual_Salary': [58000, 62000, 47000, 55000]
}
df_salary = pd.DataFrame(data_salary)

# Filter using boolean indexing
filtered_df = df_salary[df_salary['Annual_Salary'] < 60000]
print("\nEmployees with Salary < $60,000:\n", filtered_df)
