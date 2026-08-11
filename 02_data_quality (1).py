import pandas as pd
import os

# Find the project folder automatically
base_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_path, "Dataset", "Blinkit_Dataset.xlsx")

# Load the workbook
excel = pd.ExcelFile(file_path)

print("=" * 60)
print("BLINKIT DATA QUALITY REPORT")
print("=" * 60)

for sheet in excel.sheet_names:

    df = pd.read_excel(file_path, sheet_name=sheet)

    print(f"\n📄 Sheet: {sheet}")
    print("-" * 40)

    print(f"Rows            : {df.shape[0]}")
    print(f"Columns         : {df.shape[1]}")
    print(f"Missing Values  : {df.isnull().sum().sum()}")
    print(f"Duplicate Rows  : {df.duplicated().sum()}")

    print("\nColumn Data Types:")
    print(df.dtypes)

    print("\n" + "=" * 60)