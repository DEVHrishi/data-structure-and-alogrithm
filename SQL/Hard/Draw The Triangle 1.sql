/*P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

* * * * * 
* * * * 
* * * 
* * 
*
Write a query to print the pattern P(20).*/

WITH RECURSIVE n_list AS ( SELECT 20 AS n UNION ALL SELECT n - 1 FROM n_list WHERE n > 0 ) SELECT REPEAT('* ', n) FROM n_list;