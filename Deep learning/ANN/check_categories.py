import pandas as pd

df = pd.read_csv('Students Performance Dataset.csv')

categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"\nCol: {col}")
    print(df[col].unique())
    print(f"Count: {len(df[col].unique())}")
