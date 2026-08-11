import pandas as pd

# Load the Excel workbook
import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "..", "Dataset", "Blinkit_Dataset.xlsx")
# Read workbook
excel = pd.ExcelFile(file_path)

# Print all sheet names
print("Sheets in the workbook:")
print(excel.sheet_names)

print("\nSummary of each sheet:")

for sheet in excel.sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet)

    print(f"\n===== {sheet} =====")
    print("Rows :", df.shape[0])
    print("Columns :", df.shape[1])
    print("Missing Values :", df.isnull().sum().sum())