'''Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]'''

# tc: O(m*n) and sc: o(m*n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        arr = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    arr.append((row, col))
        for row, col in arr:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
            for j in range(len(matrix)):
                matrix[j][col] = 0
        return matrix

# tc: O(m*n) and sc: o(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        
        rows, cols = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][col] == 0 for col in range(cols))
        first_col_has_zero = any(matrix[row][0] == 0 for row in range(rows))
        
        # Use first row and column as markers
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        # Set the zeroes based on markers in the first row and column
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        # Set the first row and first column to zero if needed
        if first_row_has_zero:
            for col in range(cols):
                matrix[0][col] = 0
        
        if first_col_has_zero:
            for row in range(rows):
                matrix[row][0] = 0
                