import pandas as pd

# STEP 1: Load Dataset

# Reading the raw dataset from the correct folder
df = pd.read_csv("data/raw/SampleSuperstore.csv")

print("Original Data Info:")
print(df.info())

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# STEP 2: Handle Missing Values

# Separate numeric and categorical columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = df.select_dtypes(include=['object']).columns

# Fill missing values in numeric columns with mean
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Fill missing values in categorical columns with 'Unknown'
df[categorical_cols] = df[categorical_cols].fillna("Unknown")

# STEP 3: Remove Duplicate Rows

df.drop_duplicates(inplace=True)


# STEP 4: Validate Data Types

# Ensure numeric columns are properly converted
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')


# STEP 5: Verify Cleaned Data

print("\nData Info After Cleaning:")
print(df.info())

# STEP 6: Save Cleaned Dataset

# Saving cleaned dataset to the cleaned folder
df.to_csv("data/cleaned/Cleaned_SampleSuperstore.csv", index=False)

print("\nData cleaning completed successfully.")