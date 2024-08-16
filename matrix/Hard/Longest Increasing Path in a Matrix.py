'''Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1'''

# tc: O(m*n) and sc: o(m*n)
class Solution:
    def dfs(self, matrix, row, col, prev, memo):
        # boundary conditions
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            return 0
        # check if current value is greater than previous value
        if matrix[row][col] <= prev:
            return 0

        if memo[row][col] != -1:
            return memo[row][col]
        
        current_val = matrix[row][col]
        left = self.dfs(matrix, row, col-1, current_val, memo)
        right = self.dfs(matrix, row, col+1, current_val, memo)
        top = self.dfs(matrix, row-1, col, current_val, memo)
        down = self.dfs(matrix, row+1, col, current_val, memo)


        memo[row][col] = 1 + max(left , right , top , down)

        return memo[row][col]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans = float('-inf')
        memo = [[-1]*len(matrix[0]) for i in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                ans = max(ans, self.dfs(matrix, row, col, -1, memo))
        return ans