'''Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12'''

'''approach:
1. recursion
2. 2D 
3. 1D'''

# tc: o(m*n) and sc: o(m*n)
class Solution:
    def dfs(self, grid, row, col, memo):
        if row > len(grid) - 1 or col > len(grid[0])- 1:
            return float('inf')
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return grid[row][col]
        if memo[row][col] != 0:
            return memo[row][col]
        right = self.dfs(grid, row, col+1, memo)
        down = self.dfs(grid, row+1, col, memo)
        memo[row][col] = grid[row][col] + min(right, down)
        return memo[row][col]
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = [[0]*len(grid[0]) for i in range(len(grid))]
        return self.dfs(grid, 0, 0, memo)

# tc: o(m*n) and sc: o(m*n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0]*len(grid[0]) for i in range(len(grid))]
        dp[0][0] = grid[0][0]

        for col in range(1, len(grid[0])):
            dp[0][col] = dp[0][col-1] + grid[0][col]
        
        for row in range(1, len(grid)):
            dp[row][0] = dp[row-1][0] + grid[row][0]
        print(dp)
        
        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                dp[row][col] = grid[row][col] + min(dp[row-1][col], dp[row][col-1])
        return dp[-1][-1]

# tc: o(m*n) and sc: o(1)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # calculate row and column length
        r = len(grid)
        c = len(grid[0])

        # define 1D array
        dp = [0]*c
        dp[0] = grid[0][0]

        # calculate the values of array from grid
        for col in range(1, c):
            dp[col] = dp[col-1]+grid[0][col]
        print(dp)

        # calculate each array value from previous array value
        for row in range(1, r):
            dp[0] += grid[row][0]
            for col in range(1, c):
                dp[col] = min(dp[col], dp[col-1]) + grid[row][col]
        return dp[-1]
