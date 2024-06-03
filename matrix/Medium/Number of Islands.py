'''Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3'''

'''approach:
1. DFS
2. BFS'''

from typing import List

# tc: O(m*n) and sc: o(m*n)
class Solution:
    def dfs(self, grid, row, col):
        # boundary conditions
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != "1":
            return
        # Mark the cell as visited
        grid[row][col] = '#'
        # Explore all four possible directions
        self.dfs(grid, row, col-1)  # left
        self.dfs(grid, row, col+1)  # right
        self.dfs(grid, row-1, col)  # up
        self.dfs(grid, row+1, col)  # down

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    self.dfs(grid, row, col)
        return count

from typing import List
from collections import deque

# tc: O(m*n) and sc: o(min(m,n))
class Solution:
    def bfs(self, grid, row, col):
        queue = deque([(row, col)])
        while queue:
            r, c = queue.popleft()
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != "1":
                continue
            grid[r][c] = '#'  # Mark the cell as visited
            # Add all adjacent cells to the queue
            queue.append((r, c-1))  # left
            queue.append((r, c+1))  # right
            queue.append((r-1, c))  # up
            queue.append((r+1, c))  # down

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    self.bfs(grid, row, col)
        return count
