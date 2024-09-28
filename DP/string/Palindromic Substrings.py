'''Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".'''

# remember this blueprint
# tc: O(n**2) and sc: O(n**2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        t = [[False] * n for _ in range(n)]
        # t[i][j] = True : s[i:j] is a palindrome where i and j are inclusive indices

        count = 0

        for L in range(1, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1

                if i == j:
                    t[i][i] = True  # Single characters are palindromes
                elif i + 1 == j:
                    t[i][j] = (s[i] == s[j])  # Strings of 2 length
                else:
                    t[i][j] = (s[i] == s[j] and t[i + 1][j - 1])

                count += t[i][j]

        return count

# tc: O(n**2) and sc: O(n**2)
class Solution:
    def check(self, i, j, s, memo):
        if i > j:
            return True
        if memo[i][j] != -1:
            return memo[i][j]
        if s[i] == s[j]:
            memo[i][j] = self.check(i+1, j-1, s, memo)
            return memo[i][j]
        memo[i][j] = False
        return memo[i][j]
        
    def countSubstrings(self, s: str) -> int:
        count = 0
        memo = [[-1]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.check(i, j, s, memo):
                    count += 1
        return count