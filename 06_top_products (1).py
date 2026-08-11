import pandas as pd
import os

# Get project folder path
base_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_path, "Dataset", "Blinkit_Dataset.xlsx")

# Load sheets
orders = pd.read_excel(file_path, sheet_name="Orders")
products = pd.read_excel(file_path, sheet_name="Products")

# Merge Orders with Products
merged = pd.merge(orders, products, on="P_ID")

# Calculate total quantity sold for each product
top_products = (
    merged.groupby("PName")["Qty"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("=" * 60)
print("TOP 10 BEST-SELLING PRODUCTS")
print("=" * 60)
print(top_products)