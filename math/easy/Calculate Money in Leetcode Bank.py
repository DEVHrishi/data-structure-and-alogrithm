'''Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.'''

def totalMoney(self, n: int) -> int:
        count_weeks = 0
        count_days = 0
        sum_m = 0
        for i in range(n):
            count_days += 1
            sum_m += count_days + count_weeks
            if count_days == 7:
                count_weeks += 1
                count_days = 0
        return sum_m   