import pandas as pd
import numpy as np
import re

# Load dataset
file_path = r"D:\Downloads\customers.csv"
df = pd.read_csv(file_path)

# Display basic info and check missing values
print("Initial Data Overview:\n")
print(df.info())  # Check data types and missing values
print("\nMissing Values:\n", df.isnull().sum())  # Count missing values
print("\nDuplicate Records:", df.duplicated().sum())  # Count duplicate records

# Fill missing values using assignment
df = df.assign(
    name=df["name"].fillna("Unknown"),
    country=df["country"].fillna("Not Specified"),
    purchase_amount=df["purchase_amount"].fillna(df["purchase_amount"].mean())
)

print("Missing values after handling:\n", df.isnull().sum())  # Verify

# Function to validate email
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, str(email)))

# Apply validation
df["email"] = df["email"].astype(str).apply(lambda x: x if is_valid_email(x) else "Invalid")

# Check invalid emails
print("Invalid email count:", (df["email"] == "Invalid").sum())

# Function to standardize phone numbers
def standardize_phone(phone):
    phone = re.sub(r'\D', '', str(phone))  # Remove non-numeric characters
    if len(phone) == 10:
        return f"+1-{phone}"  # Assume US country code if 10 digits
    return "Invalid"

# Apply phone standardization
df["phone"] = df["phone"].astype(str).apply(standardize_phone)

# Check invalid phone numbers
print("Invalid phone count:", (df["phone"] == "Invalid").sum())

# Standardize country names
df["country"] = df["country"].str.title()

# Remove duplicates
df = df.drop_duplicates()
print("Duplicate Records After Cleaning:", df.duplicated().sum())  # Should be 0

# Remove outliers
df = df[df["purchase_amount"].notna()]  # Ensure no NaNs before calculating IQR
q1, q3 = df["purchase_amount"].quantile([0.25, 0.75])
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

df = df[(df["purchase_amount"] >= lower_bound) & (df["purchase_amount"] <= upper_bound)]

print("Outliers removed. Remaining records:", len(df))

# Save fully cleaned dataset
final_cleaned_file_path = r"D:\Downloads\customers_final.csv"
df.to_csv(final_cleaned_file_path, index=False)

print("Final cleaned dataset saved:", final_cleaned_file_path)
