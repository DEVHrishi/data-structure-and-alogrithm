'''Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.'''

# tc: O(m*n) and sc: O(m*n)
class Solution:
    def traverse(self, i, j, text1, text2, memo):
        if i >= len(text1) or j >= len(text2):
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        if text1[i] == text2[j]:
            memo[i][j] = 1 + self.traverse(i+1, j+1, text1, text2, memo)
            return memo[i][j]
        left = self.traverse(i+1, j, text1, text2, memo)
        right = self.traverse(i, j+1, text1, text2, memo)
        memo[i][j] = max(left, right)
        return memo[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1]*len(text2) for i in range(len(text1))]
        return self.traverse(0, 0, text1, text2, memo)

# tc: O(m*n) and sc: O(m*n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1]*(len(text2)+1) for i in range(len(text1)+1)]

        for i in range(len(text2)+1):
            dp[0][i] = 0
        for j in range(len(text1)+1):
            dp[j][0] = 0
        print(dp)
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]

# tc: O(m*n) and sc: O(n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Ensure text1 is the shorter string to minimize space usage
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        
        # Now text1 is shorter, and we use only 2 rows for the dp array
        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)
        
        for j in range(1, len(text2) + 1):
            for i in range(1, len(text1) + 1):
                if text1[i-1] == text2[j-1]:
                    current[i] = 1 + previous[i-1]
                else:
                    current[i] = max(previous[i], current[i-1])
            # Move the current row to the previous, and reset current
            previous, current = current, previous
        
        return previous[-1]



# print the LCS
def reconstruct_lcs(self, text1, text2, memo):
        i, j = 0, 0
        lcs = []
        while i < len(text1) and j < len(text2):
            if text1[i] == text2[j]:
                lcs.append(text1[i])
                i += 1
                j += 1
            elif memo[i+1][j] >= memo[i][j+1]:
                i += 1
            else:
                j += 1
        return ''.join(lcs)