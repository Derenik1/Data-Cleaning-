import pandas as pd

customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")
products = pd.read_csv("products.csv")
sessions = pd.read_csv("sessions.csv")
marketing = pd.read_csv("marketing.csv")
reviews = pd.read_csv("reviews.csv")

# Clean: Remove duplicates, fill or drop nulls
orders.drop_duplicates(inplace=True)
orders['order_date'] = pd.to_datetime(orders['order_date'])

# Merge key dataframes
orders_products = orders.merge(products, on='product_id', how='left')
full_data = orders_products.merge(customers, on='customer_id', how='left')
