'''Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false'''

# tc: O(m+n) and sc: O(1)
class Solution:
    def dfs(self,matrix, row, col, target):
        if col < 0 or row >= len(matrix):
            return False
        if matrix[row][col] == target:
            return True
        if target < matrix[row][col]:
            return self.dfs(matrix, row, col - 1, target)
        else:
            return self.dfs(matrix, row+1, col, target)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.dfs(matrix, 0, len(matrix[0])-1, target)

# tc: O(m+n) and sc: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # calculate the row and column length
        m = len(matrix)
        n = len(matrix[0])

        row , col = 0, n-1

        while (row < m and col >= 0):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False