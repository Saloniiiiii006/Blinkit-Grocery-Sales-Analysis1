import pandas as pd
import os

# Get the project folder path
base_path = os.path.dirname(os.path.dirname(__file__))

# Create the correct path to the Excel file
file_path = os.path.join(base_path, "Dataset", "Blinkit_Dataset.xlsx")

# Read the Ratings sheet
ratings = pd.read_excel(file_path, sheet_name="Ratings")

# Find duplicate RT_IDs
duplicate_ids = ratings[ratings.duplicated(subset=["RT_ID"], keep=False)]

# Sort duplicates by RT_ID
duplicate_ids = duplicate_ids.sort_values(by="RT_ID")

# Display the results
print("=" * 60)
print("DUPLICATE RT_ID ANALYSIS")
print("=" * 60)

print(f"\nTotal Duplicate Records: {len(duplicate_ids)}\n")

print(duplicate_ids)

print("\n" + "=" * 60)