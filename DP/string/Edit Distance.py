'''Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')'''

# tc: O(m*n) and sc: O(m*n)
class Solution:
    def traverse(self, m, n, word1, word2, memo):
        if m == 0 or n == 0:
            return m+n
        if memo[m][n] != -1:
            return memo[m][n]
        if word1[m-1] == word2[n-1]:
            memo[m][n] = self.traverse(m-1, n-1, word1, word2, memo)
            return memo[m][n]
        left = self.traverse(m-1, n, word1, word2, memo)
        right = self.traverse(m, n-1, word1, word2, memo)
        middle = self.traverse(m-1, n-1, word1, word2, memo)

        memo[m][n] = 1 + min(left, right, middle)
        return memo[m][n]
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word1)+len(word2)
        memo = [[-1]*(len(word2)+1) for _ in range(len(word1)+1)]
        self.traverse(len(word1), len(word2), word1, word2, memo)
        print(memo)
        return memo[-1][-1]

# tc: O(m*n) and sc: O(m*n)
class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word1)+len(word2)
        memo = [[-1]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i == 0 or j == 0:
                    memo[i][j] = i + j
                elif word1[i-1] == word2[j-1]:
                    memo[i][j] = memo[i-1][j-1]
                else:
                    memo[i][j] = 1 + min(memo[i-1][j], memo[i][j-1], memo[i-1][j-1])
        return memo[-1][-1]