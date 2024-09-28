'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.'''


#Approach-1 (Using Recursion + Memoization)
# tc: O(n) and sc: O(n)
class Solution:
    def fun(self, n, memo):
        if n <= 1:
            return n
        if memo[n] != -1:
            return memo[n]
        memo[n] = self.fun(n-1, memo) + self.fun(n-2, memo)
        return memo[n]
    def fib(self, n: int) -> int:
        memo = [-1] * (n+1)
        return self.fun(n, memo)
        
#Approach-2 (Using Bottom Up DP)
# tc: O(n) and sc: O(n)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        result = [-1]* (n+1)
        result[0] = 0
        result[1] = 1
        for i in range(2, n+1):
            result[i] = result[i-1]+result[i-2]
        return result[n]
    
#Approach-3 (Constant Space Complexity)
# tc: O(n) and sc: O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b, c = 0, 1, 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return c