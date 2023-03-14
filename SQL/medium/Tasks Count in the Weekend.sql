/*surface:Tasks

+-------------+------+
| Column Name | Type |
+-------------+------+
| task_id     | int  |
| assignee_id | int  |
| submit_date | date |
+-------------+------+
task_id is the primary key of this table.
Each row in this table contains a task ID, a delegate ID, and a submission date.
 

Write a SQL to query:

the number of tasks submitted during weekends (Saturday, Sunday)  weekend_cnt, and
The number of tasks submitted in a working day working_cnt.
Return the result table in any order .
The query result format is shown in the following example.

 

Example 1:

enter: 
Tasks table:
+---------+-------------+-------------+
| task_id | assignee_id | submit_date |
+---------+-------------+-------------+
| 1       | 1           | 2022-06-13  |
| 2       | 6           | 2022-06-14  |
| 3       | 6           | 2022-06-15  |
| 4       | 3           | 2022-06-18  |
| 5       | 5           | 2022-06-19  |
| 6       | 7           | 2022-06-19  |
+---------+-------------+-------------+
output: 
+-------------+-------------+
| weekend_cnt | working_cnt |
+-------------+-------------+
| 3           | 3           |
+-------------+-------------+
explain: 
Task 1 was submitted on Monday.
Task 2 was submitted on Tuesday.
Task 3 was submitted on Wednesday.
Task 4 was submitted on Saturday.
Task 5 was submitted on Sunday.
Task 6 was submitted on Sunday.
3 tasks were submitted over the weekend.
3 tasks were submitted on weekdays.*/

# Time:  O(n)
# Space: O(n)

SELECT SUM(WEEKDAY(submit_date) >= 5) AS weekend_cnt,
       SUM(WEEKDAY(submit_date) < 5) AS working_cnt
FROM Tasks;