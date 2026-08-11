import pandas as pd
import os

base_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_path, "Dataset", "Blinkit_Dataset.xlsx")

ratings = pd.read_excel(file_path, sheet_name="Ratings")

# Find duplicate rows
duplicates = ratings[ratings.duplicated(keep=False)]

print("Number of duplicate rows:", duplicates.shape[0])

print("\nDuplicate Records:\n")
print(duplicates)