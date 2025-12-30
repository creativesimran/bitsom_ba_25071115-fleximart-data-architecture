# Star Schema Design – FlexiMart Data Warehouse

# Section 1: Schema Overview

FlexiMart’s data warehouse is designed using a star schema to support efficient analytical reporting and historical sales analysis. The schema consists of one central fact table connected to multiple dimension tables.



# FACT TABLE: fact_sales

Grain:  
One row per product per order line item. Each record represents the sale of a single product in a specific order on a specific date.

Business Process:  
Sales transactions generated from customer orders.

Measures (Numeric Facts):
- quantity_sold: Number of units sold for the product
- unit_price: Price per unit at the time of sale
- discount_amount: Discount applied
- total_amount: Final sales amount calculated as  
  (quantity_sold × unit_price − discount_amount)

Foreign Keys:
- date_key → dim_date
- product_key → dim_product
- customer_key → dim_customer



# DIMENSION TABLE: dim_date

Purpose:  
Stores date-related attributes to enable time-based analysis such as daily, monthly, quarterly, and yearly trends.

Type:  
Conformed dimension shared across multiple fact tables.

Attributes:
- date_key (PK): Surrogate key in YYYYMMDD format
- full_date: Actual calendar date
- day_of_week: Day name (Monday, Tuesday, etc.)
- month: Month number (1–12)
- month_name: Month name (January, February, etc.)
- quarter: Quarter of the year (Q1, Q2, Q3, Q4)
- year: Year (2023, 2024, etc.)
- is_weekend: Boolean value indicating weekend or weekday



# DIMENSION TABLE: dim_product

Purpose:  
Stores descriptive information about products for product-based analysis.

Attributes:
- product_key (PK): Surrogate key
- product_id: Original product identifier from source system
- product_name: Name of the product
- category: Product category (Electronics, Clothing, etc.)
- brand: Product brand
- standard_price: List price of the product
- effective_start_date: Record start date (for historical tracking)
- effective_end_date: Record end date
- is_active: Indicates whether the product record is currently active



# DIMENSION TABLE: dim_customer

Purpose:  
Stores customer-related attributes for customer behavior and segmentation analysis.

Attributes:
- customer_key (PK): Surrogate key
- customer_id: Original customer identifier from source system
- first_name: Customer’s first name
- last_name: Customer’s last name
- email: Customer email address
- city: Customer city
- registration_date: Date when the customer registered
- customer_segment: Classification such as Regular, Premium, or VIP



# Summary

This star schema design enables fast query performance, simplified joins, and clear separation between measurable facts and descriptive dimensions. It supports analytical use cases such as sales trends over time, top-selling products, and customer purchasing behavior.



# Section 2: Design Decisions

The fact table is designed at the transaction line-item level, meaning each record represents one product sold in a single order. This granularity was chosen because it provides maximum analytical flexibility. It allows accurate calculation of measures such as quantity sold, revenue, discounts, and average price. From this detailed level, sales data can easily be aggregated to daily, monthly, product-level, or category-level summaries.

Surrogate keys are used instead of natural keys to ensure stability and performance in the data warehouse. Natural keys such as customer_id or product_id may change over time or differ across source systems. Surrogate keys remain constant, improve join efficiency, and support historical tracking of dimension changes without affecting existing fact records.

This star schema supports drill-down and roll-up operations efficiently. Users can drill down from year to month to day using the date dimension, or roll up sales from individual products to product categories. This design enables fast and flexible analytical reporting.

# Section 3: Sample Data Flow

This section illustrates how a single sales transaction flows from the source system into the data warehouse using the star schema.

# Source Transaction
Order #101  
Customer: John Doe  
Product: Laptop  
Quantity: 2  
Unit Price: 50,000  
Order Date: 15-Jan-2024  

# Data Warehouse Representation

# fact_sales
The transactional data is stored in the fact table with references to dimension tables using surrogate keys.

{
  date_key: 20240115,
  product_key: 5,
  customer_key: 12,
  quantity_sold: 2,
  unit_price: 50000,
  discount_amount: 0,
  total_amount: 100000
}

# dim_date
The order date is represented in the date dimension with multiple time-related attributes.

{
  date_key: 20240115,
  full_date: '2024-01-15',
  day_of_week: 'Monday',
  month: 1,
  month_name: 'January',
  quarter: 'Q1',
  year: 2024,
  is_weekend: false
}

# dim_product
The product information is stored once in the product dimension.

{
  product_key: 5,
  product_name: 'Laptop',
  category: 'Electronics',
  brand: 'Generic',
  standard_price: 50000
}

# dim_customer
Customer details are stored in the customer dimension.

{
  customer_key: 12,
  customer_name: 'John Doe',
  city: 'Mumbai',
  customer_segment: 'Regular'
}

This flow demonstrates how transactional data is separated into facts and dimensions, enabling efficient analysis without data redundancy.
