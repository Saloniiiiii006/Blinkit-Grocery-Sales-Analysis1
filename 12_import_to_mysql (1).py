import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# MySQL connection
username = "root"
password = quote_plus("Saloni@006")
host = "localhost"
database = "blinkit_analysis"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

files = {
    "customers": "../CSV_Files/Customers.csv",
    "products": "../CSV_Files/Products.csv",
    "orders": "../CSV_Files/Orders.csv",
    "transactions": "../CSV_Files/Transactions.csv",
    "ratings": "../CSV_Files/Ratings.csv",
    "delivery": "../CSV_Files/Delivery.csv",
}

for table, file in files.items():
    print(f"Importing {table}...")
    df = pd.read_csv(file)
    df.to_sql(table, engine, if_exists="replace", index=False)
    print(f"✓ {table}: {len(df)} rows imported")

print("\nAll tables imported successfully!")