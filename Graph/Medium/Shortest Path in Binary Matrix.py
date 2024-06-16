'''Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1'''

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direction = [(0, -1), (0, 1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        count  = 1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        queue = deque([(0, 0, count)])
        grid[0][0] = 1

        while queue:
            row, col, count = queue.popleft()
            if row == len(grid) - 1 and col == len(grid[0])- 1:
                return count
            
            for x, y in direction:
                dx = row + x
                dy = col + y

                if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and grid[dx][dy] == 0:
                    queue.append((dx, dy, count + 1))
                    grid[dx][dy] = 1
        return -1