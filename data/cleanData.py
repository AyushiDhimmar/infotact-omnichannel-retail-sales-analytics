import pandas as pd

# Load dataset
df = pd.read_csv("SampleSuperstore.csv")

print("Original Data Info:")
print(df.info())
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Handle Missing Values

# Separate numeric and categorical columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = df.select_dtypes(include=['object']).columns

# Fill numeric columns with mean
for col in numeric_cols:
    df[col].fillna(df[col].mean(), inplace=True)

# Fill categorical columns with "Unknown"
for col in categorical_cols:
    df[col].fillna("Unknown", inplace=True)

# Remove Duplicate Rows

df.drop_duplicates(inplace=True)

# Standardize Date Columns

# Common date column names in this dataset
date_cols = ['Order Date', 'Ship Date']

for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# Validate and Correct Data Types

# Convert columns to appropriate types (if needed)
for col in df.columns:
    # Try converting to numeric where possible
    try:
        df[col] = pd.to_numeric(df[col])
    except:
        pass  # keep original if conversion fails

print("\nData Info After Cleaning:")
print(df.info())

# Save Cleaned Dataset
df.to_csv("Cleaned_SampleSuperstore.csv", index=False)

print("\nData cleaning completed and saved as 'Cleaned_SampleSuperstore.csv'")