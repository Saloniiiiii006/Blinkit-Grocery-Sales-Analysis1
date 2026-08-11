import pandas as pd
import os

# Get project folder path
base_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_path, "Dataset", "Blinkit_Dataset.xlsx")

# Load Customers sheet
customers = pd.read_excel(file_path, sheet_name="Customers")

print("=" * 60)
print("CUSTOMER ANALYSIS")
print("=" * 60)

# Total Customers
print(f"\nTotal Customers: {customers['C_ID'].nunique()}")

# Customers by Gender
print("\nCustomers by Gender")
print(customers["gender"].value_counts())

# Customers by City
print("\nTop 10 Cities")
print(customers["City"].value_counts().head(10))

# Customers by State
print("\nTop 10 States")
print(customers["State"].value_counts().head(10))

# Age Statistics
print("\nAge Statistics")
print(customers["Age"].describe())