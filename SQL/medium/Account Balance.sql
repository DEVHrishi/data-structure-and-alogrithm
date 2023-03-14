/*Table Name:Transactions

+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| day         | date |
| type        | ENUM |
| amount      | int  |
+-------------+------+
(account_id, day) is the primary key of the Transactions table.
Each row of data in the table represents the information of a transaction, including the transaction account (account_id), transaction type (type), transaction time (day), and transaction amount (amount).
The transaction type (type) field includes two behaviors: deposit ('Deposit'), withdrawal ('Withdraw').
 

Please write the account balance that can return the user after each transaction is completed. We agree that the account balance of all users is 0 before the transaction, and ensure that the balance after all transactions is not negative.

Please sort the returned results in ascending orderaccount_id according to account ( ), date (  day )  .

Please refer to the following test sample for the format of query results.

 

Test example 1:

enter: 
Transactions table:
+------------+------------+----------+--------+
| account_id | day        | type     | amount |
+------------+------------+----------+--------+
| 1          | 2021-11-07 | Deposit  | 2000   |
| 1          | 2021-11-09 | Withdraw | 1000   |
| 1          | 2021-11-11 | Deposit  | 3000   |
| 2          | 2021-12-07 | Deposit  | 7000   |
| 2          | 2021-12-12 | Withdraw | 7000   |
+------------+------------+----------+--------+

output: 
+------------+------------+---------+
| account_id | day        | balance |
+------------+------------+---------+
| 1          | 2021-11-07 | 2000    |
| 1          | 2021-11-09 | 1000    |
| 1          | 2021-11-11 | 4000    |
| 2          | 2021-12-07 | 7000    |
| 2          | 2021-12-12 | 0       |
+------------+------------+---------+

explain: 
Account 1:
- The initial amount is 0.
- 2021-11-07 --> Deposit 2000. The balance becomes 0 + 2000 = 2000.
- 2021-11-09 --> Withdraw 1000. The balance becomes 2000 - 1000 = 1000.
- 2021-11-11 --> deposit 3000. The balance becomes 1000 + 3000 = 4000.
Account 2:
- The initial amount is 0.
- 2021-12-07 --> Deposit 7000. The balance becomes 0 + 7000 = 7000.
- 2021-12-12 --> Withdraw 7000. The balance becomes 7000 - 7000 = 0.*/

# Time:  O(nlogn)
# Space: O(n)

SELECT account_id, day,
       SUM(CASE WHEN type = 'DEPOSIT' THEN amount ELSE -amount END)
       OVER (PARTITION BY account_id ORDER BY day) AS balance
FROM Transactions;