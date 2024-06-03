'''You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0'''

# tc: O(m*n) and sc: o(m*n)
class Solution:
    def dfs(self, grid, row, col):
        print(row, col)
        # boundary conditions
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
            return 0
        # mark as visited
        grid[row][col] = 0
        # move top, down, left, right
        top = self.dfs(grid, row-1, col)
        down = self.dfs(grid, row+1, col)
        left = self.dfs(grid, row, col-1)
        right = self.dfs(grid, row, col+1)

        return 1 + top + down + left + right
        

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    ans = max(ans, self.dfs(grid, row, col))
        return ans
    
# tc: O(m*n) and sc: o(m*n)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = 0
                    stack = [(row, col)]
                    while stack:
                        r, c = stack.pop()
                        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                            continue
                        grid[r][c] = 0
                        area += 1
                        for dr, dc in directions:
                            stack.append((r + dr, c + dc))
                    max_area = max(max_area, area)
                    
        return max_area
