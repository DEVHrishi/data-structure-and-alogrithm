'''Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

Example 1:


Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.'''

# tc: o(m*n) and sc: o(1)
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] != matrix[row-1][col-1]:
                    return False
        return True

# tc: o(m*n) and sc: o(1)
class Solution:
    def helper(self, matrix: List[List[int]], row: int, col: int) -> bool:
        if row >= len(matrix):
            return True
        
        if col >= len(matrix[0]):
            return self.helper(matrix, row + 1, 1)
        
        if row > 0 and col > 0 and matrix[row][col] != matrix[row - 1][col - 1]:
            return False
        
        return self.helper(matrix, row, col + 1)
        
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return self.helper(matrix, 1, 1)

# follow up 1
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def load_row(matrix, index):
            return matrix[index] if index < len(matrix) else None
    
        prev_row = load_row(matrix, 0)
        for row_index in range(1, len(matrix)):
            current_row = load_row(matrix, row_index)
            for col in range(1, len(current_row)):
                if current_row[col] != prev_row[col - 1]:
                    return False
            prev_row = current_row
        
        return True