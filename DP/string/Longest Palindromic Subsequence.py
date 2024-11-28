'''Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".'''

class Solution:
    def recursion(self, s, i, j, memo):
        if i > j:
            return 0
        if i == j:
            return 1
        if memo[i][j] != -1:
            return memo[i][j]
            
        if s[i] == s[j]:
            memo[i][j] = 2 + self.recursion(s, i + 1, j-1, memo)
            
        else:
            memo[i][j] = max(self.recursion(s, i+1, j, memo) , self.recursion(s, i, j-1, memo))
        return memo[i][j]
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        i, j = 0, n-1
        memo = [[-1]*n for _ in range(n)]
        return self.recursion(s, i, j, memo)
    
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        mx = float('-inf')
        for i in range(n):
            dp[i][i] = 1
            mx = max(mx, dp[i][i])
        for L in range(2, n+1):
            for i in range(n-L+1):
                j = i+L-1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j] , dp[i][j-1])
                mx = max(mx, dp[i][j])
        return mx