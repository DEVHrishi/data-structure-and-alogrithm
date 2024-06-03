'''Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false'''

# tc: O(m×n×3^L) and sc: O(L)
class Solution:
    def dfs(self, board, word, row, col, index):
        # boundary conditions
        if index == len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index]:
            return False
        
        # Mark the cell as visited
        temp = board[row][col]
        board[row][col] = '#'

        # Explore all possible directions
        found = (
            self.dfs(board, word, row, col-1, index + 1) or
            self.dfs(board, word, row, col+1, index + 1) or
            self.dfs(board, word, row-1, col, index + 1) or
            self.dfs(board, word, row+1, col, index + 1)
        )

        # Unmark the cell
        board[row][col] = temp

        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.dfs(board, word, row, col, 0):
                        return True
        return False