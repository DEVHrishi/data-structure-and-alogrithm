'''You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1'''

# tc: o(m*n) and sc: o(m*n)
class Solution:
    def dfs(self, mat, i, j, memo):
        if i >= len(mat)-1 and j >= len(mat[0])-1 and mat[i][j] != 1:
            return 1
        if i > len(mat)-1 or j > len(mat[0])-1 :

            return 0
        if mat[i][j] == 1:
            return 0
        if memo[i][j] != 0:
            return memo[i][j]
        memo[i][j] = self.dfs(mat, i+1,j, memo) + self.dfs(mat, i, j+1, memo)
        return memo[i][j]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo= [[0]*len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        return self.dfs(obstacleGrid, 0, 0, memo)
        
# tc: o(m*n) and sc: o(n)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1  # Start point
        
        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                elif col > 0:
                    dp[col] += dp[col - 1]
        
        return dp[-1]