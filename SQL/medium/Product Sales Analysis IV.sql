/*surface:Sales

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| user_id     | int   |
| quantity    | int   |
+-------------+-------+
sale_id is the primary key of this table.
product_id is a foreign key to the product table.
Each row of the table shows the ID of the product and the quantity purchased by the user.
 

surface:Product

+-------------+------+
| Column Name | Type |
+-------------+------+
| product_id  | int  |
| price       | int  |
+-------------+------+
product_id is the primary key of the table
Each row of this table represents the price of each product.
 

Write a SQL query to get, for each user, the product ids that they spend the most on. If the same user spent the most money on two or more products, get all the products that spent the most money.

Return the result table in any order .

The query result format is as follows.

 

Example 1:

enter: 
Sales table:
+---------+------------+---------+----------+
| sale_id | product_id | user_id | quantity |
+---------+------------+---------+----------+
| 1       | 1          | 101     | 10       |
| 2       | 3          | 101     | 7        |
| 3       | 1          | 102     | 9        |
| 4       | 2          | 102     | 6        |
| 5       | 3          | 102     | 10       |
| 6       | 1          | 102     | 6        |
+---------+------------+---------+----------+
Product table:
+------------+-------+
| product_id | price |
+------------+-------+
| 1          | 10    |
| 2          | 25    |
| 3          | 15    |
+------------+-------+
output: 
+---------+------------+
| user_id | product_id |
+---------+------------+
| 101     | 3          |
| 102     | 1          |
| 102     | 2          |
| 102     | 3          |
+---------+------------+ 
explain: 
User 101:
    - Spend 10 * 10 = 100 on product 1.
    - Spend 7 * 15 = 105 on product 3.
User 101 spends the most money on product 3.
User 102:
    - spend (9 + 7)* 10 = 150 on product 1
    - spend 6 * 25 = 150 on product 2
    - Spend 10 * 15 = 150 on product 3.
User 102 spends the most money on products 1, 2, and 3.*/

-- Time:  O(nlogn)
-- Space: O(n)

WITH spending_cte AS (
    SELECT s.user_id,
           s.product_id,
           RANK() OVER(PARTITION BY s.user_id ORDER BY SUM(s.quantity * p.price) DESC) AS rnk
    FROM Sales s INNER JOIN Product p ON s.product_id = p.product_id
    GROUP BY s.user_id, s.product_id
    ORDER BY NULL
)

SELECT user_id, product_id
FROM spending_cte
WHERE rnk = 1;