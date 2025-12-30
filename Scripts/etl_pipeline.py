import pandas as pd
import mysql.connector
from dateutil import parser

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Simran76",
    database="fleximart"
)
cursor = conn.cursor()
print("Database connected successfully")


cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
cursor.execute("TRUNCATE TABLE order_items")
cursor.execute("TRUNCATE TABLE orders")
cursor.execute("TRUNCATE TABLE products")
cursor.execute("TRUNCATE TABLE customers")
cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
conn.commit()
print("Old data removed from tables")


customers = pd.read_csv("C:/Users/Simran Jaiswal/Desktop/fleximart/Data/customers_raw.csv")

customers = customers.drop_duplicates()
customers = customers.dropna(subset=["email"])

def format_phone(phone):
    phone = str(phone).replace(" ", "").replace("-", "").replace("+91", "")
    if phone.startswith("0"):
        phone = phone[1:]
    return "+91-" + phone

customers["phone"] = customers["phone"].apply(format_phone)
customers["registration_date"] = customers["registration_date"].apply(
    lambda x: parser.parse(str(x), dayfirst=True).date()
)
customers["city"] = customers["city"].str.title()


insert_customer_query = """
INSERT INTO customers (first_name, last_name, email, phone, city, registration_date)
VALUES (%s, %s, %s, %s, %s, %s)
"""

customer_id_mapping = {}

for _, row in customers.iterrows():
    cursor.execute(
        insert_customer_query,
        (
            row["first_name"],
            row["last_name"],
            row["email"],
            row["phone"],
            row["city"],
            row["registration_date"]
        )
    )
    customer_id_mapping[row["customer_id"]] = cursor.lastrowid

conn.commit()
print(" Customers loaded")


products = pd.read_csv("C:/Users/Simran Jaiswal/Desktop/fleximart/Data/products_raw.csv")

products["category"] = products["category"].str.strip().str.capitalize()
products["price"] = products["price"].fillna(products["price"].mean())
products["stock_quantity"] = products["stock_quantity"].fillna(0).astype(int)



insert_product_query = """
INSERT INTO products (product_name, category, price, stock_quantity)
VALUES (%s, %s, %s, %s)
"""

product_id_mapping = {}

for _, row in products.iterrows():
    try:
        cursor.execute(
            insert_product_query,
            (
                row["product_name"],   
                row["category"],
                row["price"],
                row["stock_quantity"]
            )
        )
        product_id_mapping[row["product_id"]] = cursor.lastrowid
    except Exception as e:
        print("❌ Error inserting product:", row["product_name"])
        print(e)

conn.commit()
print(" Products loaded successfully")


sales = pd.read_csv("C:/Users/Simran Jaiswal/Desktop/fleximart/Data/sales_raw.csv")

sales = sales.rename(columns={
    "transaction_id": "order_id",
    "transaction_date": "order_date"
})

sales["order_date"] = sales["order_date"].apply(
    lambda x: parser.parse(str(x), dayfirst=True).date()
)

sales["subtotal"] = sales["quantity"] * sales["unit_price"]

sales = sales.drop_duplicates(subset=["order_id"])
sales = sales.dropna(subset=["customer_id", "product_id"])


valid_customers = set(customer_id_mapping.keys())

before = sales.shape[0]
sales = sales[sales["customer_id"].isin(valid_customers)]
after = sales.shape[0]

print("Sales removed due to missing customer mapping:", before - after)



order_totals = (
    sales.groupby("order_id")
    .agg({
        "customer_id": "first",
        "order_date": "first",
        "subtotal": "sum"
    })
    .reset_index()
)

insert_order_query = """
INSERT INTO orders (customer_id, order_date, total_amount, status)
VALUES (%s, %s, %s, %s)
"""

order_id_mapping = {}

for _, row in order_totals.iterrows():
    cursor.execute(
        insert_order_query,
        (
            customer_id_mapping[row["customer_id"]],  
            row["order_date"],
            row["subtotal"],
            "Completed"
        )
    )
    order_id_mapping[row["order_id"]] = cursor.lastrowid

conn.commit()
print(" Orders loaded")


insert_item_query = """
INSERT INTO order_items (order_id, product_id, quantity, unit_price, subtotal)
VALUES (%s, %s, %s, %s, %s)
"""

for _, row in sales.iterrows():
    cursor.execute(
        insert_item_query,
        (
            order_id_mapping[row["order_id"]],
            product_id_mapping[row["product_id"]],
            row["quantity"],
            row["unit_price"],
            row["subtotal"]
        )
    )

conn.commit()
print("Order items loaded")

cursor.close()
conn.close()
print(" ETL Pipeline completed successfully")

