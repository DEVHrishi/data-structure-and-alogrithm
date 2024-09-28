'''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step'''

'''approach:
1. recursive
2. tabulation
3. space optimize'''

# Approach-1 (Recursion with Memo) : Top Down
# tc: O(n) and sc: O(n)
class Solution:
    def fib(self, n, dp):
        if n < 1:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        elif dp[n] != -1:
            return dp[n]
        else:
            dp[n] = self.fib(n-1, dp) + self.fib(n-2, dp)
            return dp[n]
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.fib(n, dp)
    

# Approach-2 (Using Bottom Up DP)
# tc: O(n) and sc: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
    
# Approach-3 (Improving approach-2) -
# tc: O(n) and sc: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        a, b, c = 1, 1, 2
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return c