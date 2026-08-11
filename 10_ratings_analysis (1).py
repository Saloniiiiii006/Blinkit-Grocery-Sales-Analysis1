import pandas as pd
import os

# Get project folder path
base_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_path, "Dataset", "Blinkit_Dataset.xlsx")

# Load Ratings sheet
ratings = pd.read_excel(file_path, sheet_name="Ratings")

print("=" * 60)
print("CUSTOMER RATINGS ANALYSIS")
print("=" * 60)

# Average Ratings
avg_product = ratings["Prod_Rating"].mean()
avg_delivery = ratings["Delivery/Service_Rating"].mean()

print(f"\nAverage Product Rating   : {avg_product:.2f}")
print(f"Average Delivery Rating : {avg_delivery:.2f}")

# Count of ratings received
product_count = ratings["Prod_Rating"].count()
delivery_count = ratings["Delivery/Service_Rating"].count()

print(f"\nProduct Ratings Given   : {product_count}")
print(f"Delivery Ratings Given  : {delivery_count}")

# Rating Percentage
total_orders = len(ratings)

print(f"\nPercentage Product Ratings  : {(product_count/total_orders)*100:.2f}%")
print(f"Percentage Delivery Ratings : {(delivery_count/total_orders)*100:.2f}%")
