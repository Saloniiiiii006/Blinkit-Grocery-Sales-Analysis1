import pandas as pd
import os

# Project folder path
base_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_path, "Dataset", "Blinkit_Dataset.xlsx")

# Load sheets
orders = pd.read_excel(file_path, sheet_name="Orders")
products = pd.read_excel(file_path, sheet_name="Products")

# Merge data
merged = pd.merge(orders, products, on="P_ID")

# Revenue per order
merged["Revenue"] = merged["Qty"] * merged["Price"]

# Category summary
category_summary = (
    merged.groupby("Category")
    .agg(
        Total_Quantity=("Qty", "sum"),
        Total_Revenue=("Revenue", "sum")
    )
    .sort_values("Total_Revenue", ascending=False)
)

print("=" * 60)
print("CATEGORY PERFORMANCE")
print("=" * 60)
print(category_summary)