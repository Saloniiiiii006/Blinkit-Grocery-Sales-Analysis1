import pandas as pd
import os

# Get the project folder path
base_path = os.path.dirname(os.path.dirname(__file__))

# Path to the Excel file
file_path = os.path.join(base_path, "Dataset", "Blinkit_Dataset.xlsx")

# Read the required sheets
orders = pd.read_excel(file_path, sheet_name="Orders")
products = pd.read_excel(file_path, sheet_name="Products")
customers = pd.read_excel(file_path, sheet_name="Customers")

# Merge Orders and Products using Product ID
merged = pd.merge(orders, products, on="P_ID")

# Create Revenue column
merged["Revenue"] = merged["Qty"] * merged["Price"]

# Calculate KPIs
total_revenue = merged["Revenue"].sum()
total_orders = orders["Or_ID"].nunique()
total_customers = customers["C_ID"].nunique()
total_products = products["P_ID"].nunique()
average_order_value = total_revenue / total_orders

# Print Results
print("=" * 60)
print("          BLINKIT BUSINESS OVERVIEW")
print("=" * 60)

print(f"Total Revenue         : ₹{total_revenue:,.2f}")
print(f"Total Orders          : {total_orders}")
print(f"Total Customers       : {total_customers}")
print(f"Total Products        : {total_products}")
print(f"Average Order Value   : ₹{average_order_value:,.2f}")

print("=" * 60)