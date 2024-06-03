'''Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]'''

# tc: o(m*n) and sc: o(m*n)
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result_matrix = [[0]*len(matrix) for i in range(len(matrix[0]))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                    result_matrix[col][row] = matrix[row][col]
        return result_matrix

# tc: o(m*n) and sc: o(m*n)
class Solution:
    def traverse(self, matrix, row, col, result_matrix):
        if row == len(matrix)-1 and col == len(matrix[0])-1:
            result_matrix[col][row] = matrix[row][col]
            return
        result_matrix[col][row] = matrix[row][col]
        if col < len(matrix[0])-1:
            self.traverse(matrix, row, col+1, result_matrix)
        elif row < len(matrix)-1:
            self.traverse(matrix, row+1, 0, result_matrix)

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result_matrix = [[0]*len(matrix) for i in range(len(matrix[0]))]
        self.traverse(matrix, 0, 0, result_matrix)
        return result_matrix