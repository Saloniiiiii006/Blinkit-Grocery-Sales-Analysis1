import pandas as pd
import os

excel_file = excel_file = "/Users/saloni/Desktop/Project folder/Dataset/Blinkit_Dataset.xlsx"
output_folder = output_folder = "/Users/saloni/Desktop/Project folder/CSV_Files"
os.makedirs(output_folder, exist_ok=True)

xls = pd.ExcelFile(excel_file)

for sheet in xls.sheet_names:
    df = pd.read_excel(excel_file, sheet_name=sheet)

    # Remove line breaks from all text columns
    df = df.replace({r'[\r\n]+': ' '}, regex=True)

    csv_file = os.path.join(output_folder, f"{sheet}.csv")
    df.to_csv(csv_file, index=False, encoding="utf-8")

    print(f"Saved: {sheet}.csv")

print("\nAll CSV files created successfully!")