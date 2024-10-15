'''Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"'''

class Solution:
    def solve(self, i, j, s, memo):
        if i >= j:
            return True
        if memo[i][j] != -1:
            return memo[i][j]
        if s[i] == s[j]:
            memo[i][j] = self.solve(i+1, j-1, s, memo)
            return memo[i][j]
        memo[i][j] = False
        return memo[i][j]
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = [[-1]*n for _ in range(n)]
        max_len = float('-inf')
        sp = 0
        for i in range(n):
            for j in range(i, n):
                
                if self.solve(i, j, s, memo):
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        sp = i
        return s[sp: sp +max_len]