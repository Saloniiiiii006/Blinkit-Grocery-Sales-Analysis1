import pandas as pd
import os

# Get project folder path
base_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_path, "Dataset", "Blinkit_Dataset.xlsx")

# Load Transactions sheet
transactions = pd.read_excel(file_path, sheet_name="Transactions")

print("=" * 60)
print("PAYMENT METHOD ANALYSIS")
print("=" * 60)

# Payment Method Distribution
payment_summary = transactions["Transaction_Mode"].value_counts()

print("\nPayment Method Usage")
print(payment_summary)

# Percentage Distribution
payment_percentage = (
    transactions["Transaction_Mode"]
    .value_counts(normalize=True) * 100
)

print("\nPayment Method Percentage (%)")
print(payment_percentage.round(2))
