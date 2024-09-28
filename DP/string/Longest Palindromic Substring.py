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

# tc: O(n**2) and sc: O(n**2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = [[False]*len(s) for _ in range(len(s))]
        result = ''
        for L in range(1, len(s)+1):
            for i in range(len(s)-L+1):
                j = i + L - 1
                if i == j:
                    memo[i][j] = True
                elif i+1 == j:
                    memo[i][j] = (s[i] == s[j])
                else:
                    memo[i][j] = (s[i] == s[j] and memo[i+1][j-1])
                if memo[i][j] and j-i+1 > len(result):
                    result = s[i:j+1]
        return result
