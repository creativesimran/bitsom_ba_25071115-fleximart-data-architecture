
# FlexiMart Data Architecture Project

**Student Name:** Simran Jaiswal  
**Student ID:** bitsom_ba_25071115
**Email:** simranjaiswal4976@gmail.com
**Date:** 30 December 2025

---

## Project Overview

This project implements an end-to-end data architecture solution for FlexiMart, an e-commerce company. It includes building an ETL pipeline from raw CSV data into a relational database, executing business analytics queries, performing NoSQL analysis using MongoDB, and designing a data warehouse with a star schema for advanced analytical reporting.

---

## Repository Structure

```

FLEXIMART/
├── Data/
│   ├── customers_raw.csv
│   ├── products_raw.csv
│   └── sales_raw.csv
│
├── Datawarehouse/
│   ├── star_schema_design.md
│   ├── warehouse_schema.sql
│   ├── warehouse_data.sql
│
├── schema_documentation.md
├── nosql_analysis.md
│
├── Scripts/
│   ├── etl_pipeline.py
│   ├── business_queries.sql
│   ├── analytics_queries.sql
│   └── mongodb_operations.js
│
└── README.md

````

---

## Technologies Used

- Python 3.x  
- pandas  
- mysql-connector-python  
- MySQL 8.0  
- MongoDB 6.0  

---

## Setup Instructions

### MySQL Setup

```sql
CREATE DATABASE fleximart;
CREATE DATABASE fleximart_dw;
````

### Run ETL Pipeline

```bash
python Scripts/etl_pipeline.py
```

### Run Business Queries

```bash
mysql -u root -p fleximart < Scripts/business_queries.sql
```

### Data Warehouse Setup

```bash
mysql -u root -p fleximart_dw < Datawarehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < Datawarehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < Scripts/analytics_queries.sql
```

---

### MongoDB Setup

```bash
mongosh < Scripts/mongodb_operations.js
```

---

## Key Learnings

* Built a complete ETL pipeline handling real-world data quality issues
* Designed normalized relational schemas and dimensional star schemas
* Wrote advanced SQL queries including aggregations and window functions
* Understood when and why to use NoSQL databases like MongoDB

---

## Challenges Faced

1. Handling foreign key constraints while loading fact tables in the data warehouse
2. Designing realistic sample data that satisfies analytical requirements




