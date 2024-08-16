'''Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0'''

# tc: O(m*n) and sc: o(1)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col]= int(matrix[row][col])
                if (row != 0 and col != 0 and matrix[row][col] == 1):
                    matrix[row][col] = 1 + min(matrix[row][col-1], matrix[row-1][col], matrix[row-1][col-1])
                ans = max(ans, matrix[row][col])
        return ans*ans
    
# tc: O(m*n) and sc: o(m*n)
from typing import List

class Solution:
    def dp(self, matrix, r, c, memo):
            if r >= len(matrix) or c >= len(matrix[0]) or matrix[r][c] == "0":
                return 0

            if memo[r][c] != -1:
                return memo[r][c]

            down = self.dp(matrix, r + 1, c, memo)
            right = self.dp(matrix, r, c + 1, memo)
            diag = self.dp(matrix, r + 1, c + 1, memo)
            
            memo[r][c] = 1 + min(down, right, diag)
            return memo[r][c]

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        row, col = len(matrix), len(matrix[0])
        memo = [[-1] * col for _ in range(row)]  # Initialize the memoization table

        max_side = 0
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == "1":
                    max_side = max(max_side, self.dp(matrix, r, c, memo))

        return max_side ** 2

l = Solution()
matrix = [["0","1"],["1","0"]]
print(l.maximalSquare(matrix))