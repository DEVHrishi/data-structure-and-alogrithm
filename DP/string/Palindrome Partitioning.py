'''Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start, len(s)):
                if s[start:end+1] == s[start:end+1][::-1]:  # Check palindrome
                    path.append(s[start:end+1])
                    backtrack(end + 1, path)
                    path.pop()

        result = []
        backtrack(0, [])
        return result
    
class Solution:
    def backtrack(self, s, idx, curr, dp, result):
        if idx == len(s):
            result.append(curr)
            return
        for j in range(idx, len(s)):
            sol = s[idx: j+1]
            if dp[idx][j]:
                self.backtrack(s, j+1, curr+[sol], dp, result)
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for L in range(2, n+1):
            for i in range(n-L+1):
                j = i + L - 1
                if L == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = ((s[i] == s[j]) and dp[i+1][j-1])
        result = []
        self.backtrack(s, 0, [], dp, result)
        return result