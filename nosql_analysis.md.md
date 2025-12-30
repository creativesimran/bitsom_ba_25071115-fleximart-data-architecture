# NoSQL Database Analysis – FlexiMart

# Section A: Limitations of RDBMS

Relational databases like MySQL work well for structured and fixed data models, but they face limitations when handling highly diverse product information. In FlexiMart, different product categories have different attributes. For example, laptops require specifications such as RAM, processor, and storage, while shoes require size, color, and material. In an RDBMS, this would require many nullable columns or multiple additional tables, making the schema complex and inefficient.

Another challenge is frequent schema changes. Whenever a new product type is introduced, the relational schema must be altered using ALTER TABLE commands. These changes can cause downtime, increase maintenance effort, and slow down development. Managing evolving schemas becomes difficult as the product catalog grows.

Storing customer reviews is also problematic in relational databases. Reviews require multiple related tables and joins to store ratings, comments, and review dates. This increases query complexity and impacts performance when fetching complete product details along with reviews.


# Section B: Benefits of MongoDB

MongoDB addresses these issues using a flexible, schema-less document model. Each product is stored as a document, allowing different products to have different fields. Laptops, shoes, and groceries can store their specific attributes without affecting other documents, making the system highly adaptable.

MongoDB supports embedded documents, which allows customer reviews to be stored directly inside the product document. Ratings, comments, and review dates can be retrieved in a single query, improving performance and simplifying data access.

Additionally, MongoDB supports horizontal scalability through sharding. As FlexiMart’s product catalog and user base grow, data can be distributed across multiple servers, ensuring high availability and better performance for large-scale applications.


# Section C: Trade-offs of Using MongoDB

One disadvantage of MongoDB is the lack of built-in relational constraints such as foreign keys. Data consistency must be handled at the application level, which increases development responsibility.

Another drawback is that complex analytical queries and transactional reporting are generally easier in relational databases. For scenarios requiring strict ACID compliance and advanced SQL analytics, MySQL may still be more suitable than MongoDB.
