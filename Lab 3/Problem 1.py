import pandas as pd

df = pd.read_csv('train.csv')

print(" First 10 Rows ")
print(df.head(10))

print("\n Shape (rows, columns) ")
print(df.shape)

print("\n Column Names ")
print(df.columns.tolist())

print("\n Data Types ")
print(df.dtypes)

print("\n Descriptive Statistics ")
print(df.describe())
