'''Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]'''

'''approach:
1. DFS
2. BFS'''

# tc: O(m*n) and sc: o(1)
class Solution:
    def dfs(self, board, row, col):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != 'O':
            return
        board[row][col] = 'B'
        self.dfs(board, row, col + 1)
        self.dfs(board, row, col - 1)
        self.dfs(board, row - 1, col)
        self.dfs(board, row + 1, col)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if row == 0 or row == len(board)- 1 or col == 0 or col == len(board[0]) - 1:
                    self.dfs(board, row, col)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'B':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'
                    

from collections import deque
# tc: O(m*n) and sc: o(min(m,n))
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows, cols = len(board), len(board[0])
        queue = deque()

        # Helper function to mark 'O's connected to borders
        def bfs(row, col):
            if board[row][col] != 'O':
                return
            queue.append((row, col))
            board[row][col] = 'N'  # Mark the cell to avoid revisiting
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                        board[nr][nc] = 'N'
                        queue.append((nr, nc))

        # Process the border rows and columns
        for row in range(rows):
            bfs(row, 0)
            bfs(row, cols - 1)

        for col in range(cols):
            bfs(0, col)
            bfs(rows - 1, col)

        # Flip all remaining 'O's to 'X' and revert 'N' back to 'O'
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'N':
                    board[row][col] = 'O'
