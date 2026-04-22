import pandas as pd

df = pd.read_csv("SampleSuperstore.csv")

# Check missing values
print("Missing values:\n", df.isnull().sum())

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)
df.fillna("Unknown", inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("Data Cleaned")