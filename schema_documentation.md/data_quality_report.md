# FlexiMart Database Schema Documentation

# 1. Entity–Relationship Description

# ENTITY: customers
Purpose:
Stores master information about customers registered on the FlexiMart platform.

Attributes:
- customer_id: Unique identifier (Primary Key, auto-increment)
- first_name: Customer’s first name
- last_name: Customer’s last name
- email: Customer’s email address (Unique)
- phone: Customer contact number
- city: City of residence
- registration_date: Date of registration

Relationships:
- One customer can place MANY orders (1:M relationship with orders)


# ENTITY: products
Purpose:
Stores information about products available for sale.

Attributes:
- product_id: Unique identifier (Primary Key)
- product_name: Name of the product
- category: Product category
- price: Product price
- stock_quantity: Available stock

Relationships:
- One product can appear in MANY order items (1:M relationship with order_items)


# ENTITY: orders
Purpose:
Stores order-level information.

Attributes:
- order_id: Unique identifier (Primary Key)
- customer_id: References customers.customer_id
- order_date: Date of order
- total_amount: Total order value
- status: Order status

Relationships:
- One customer can place MANY orders
- One order can have MANY order items



# ENTITY: order_items
Purpose:
Stores line-item details for orders.

Attributes:
- order_item_id: Unique identifier (Primary Key)
- order_id: References orders.order_id
- product_id: References products.product_id
- quantity: Quantity ordered
- unit_price: Price per unit
- subtotal: Quantity × unit_price

Relationships:
- Many order items belong to ONE order
- Many order items reference ONE product


# 2. Normalization Explanation (3NF)

The FlexiMart database schema is designed in Third Normal Form (3NF) to eliminate redundancy and ensure data integrity. Each table has a primary key, and all non-key attributes are fully dependent on that key.

Functional dependencies are clearly defined: customer details depend only on customer_id, product attributes depend only on product_id, and order details depend on order_id. The order_items table resolves the many-to-many relationship between orders and products by storing transactional data such as quantity and price at the time of purchase.

The schema avoids update anomalies by storing customer and product data in separate tables, so updates occur in only one place. Insert anomalies are avoided because customers and products can be added independently of orders. Delete anomalies are prevented because deleting an order does not remove customer or product records.

This design satisfies 1NF through atomic attributes, 2NF by eliminating partial dependencies, and 3NF by removing transitive dependencies, making the database scalable and consistent.


# 3. Sample Data Representation

# customers
| customer_id | first_name | last_name | email |
|------------|------------|-----------|-------|
| 1 | Rahul | Sharma | rahul.sharma@gmail.com |
| 2 | Priya | Patel | priya.patel@yahoo.com |

# products
| product_id | product_name | category | price |
|-----------|--------------|----------|-------|
| 1 | Samsung Galaxy S21 | Electronics | 45999 |
| 2 | Nike Running Shoes | Fashion | 3499 |

# orders
| order_id | customer_id | order_date | total_amount |
|---------|-------------|------------|--------------|
| 1 | 1 | 2024-01-15 | 45999 |
| 2 | 2 | 2024-01-16 | 5998 |

# order_items
| order_item_id | order_id | product_id | quantity | subtotal |
|--------------|----------|------------|----------|----------|
| 1 | 1 | 1 | 1 | 45999 |
| 2 | 2 | 2 | 2 | 5998 |
