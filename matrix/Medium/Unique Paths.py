'''There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down'''

'''approach:
1. 1D
2. 2D
3. recursive'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n
        for i in range(m-1):
            new_row = [1]*n
            for j in range(n-2, -1, -1):
                new_row[j] = new_row[j+1] + row[j]
            row = new_row
        return row[0]
    
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                    grid[row][col] = grid[row-1][col]+grid[row][col-1]
        return grid[-1][-1]

class Solution:
    def dfs(self, row, col, m, n, memo):
        if row == m - 1 and col == n - 1:                
            return 1
        if row > m - 1 or col > n - 1:
            return 0
        if memo[row][col] != 0:
            return memo[row][col]
        memo[row][col] = self.dfs(row+1, col, m, n, memo) + self.dfs(row, col+1, m, n, memo)
        return memo[row][col]

    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0]*n for i in range(m)]
        return self.dfs(0, 0, m, n, memo) 