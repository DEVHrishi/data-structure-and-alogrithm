'''Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) -1 
        result = []
        while left <= right and top <= bottom:
            print(left, right, top, bottom)
            for row in range(left, right+1):
                result.append(matrix[top][row])
            top += 1
            for col in range(top, bottom+1):
                result.append(matrix[col][right])
            right -= 1
            
            if top <= bottom:
                for row in range(right, left-1, -1):
                    result.append(matrix[bottom][row])
                bottom -= 1

            if left <= right:
                for col in range(bottom, top-1, -1):
                    result.append(matrix[col][left])
                left += 1
        return result


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        def spiral_helper(matrix, top, bottom, left, right):
            if top > bottom or left > right:
                return []

            result = []

            # Traverse top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])

            # Traverse right column
            for row in range(top + 1, bottom + 1):
                result.append(matrix[row][right])

            # Traverse bottom row
            if top < bottom:  # Avoid duplicate traversal for single row
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom][col])

            # Traverse left column
            if left < right:  # Avoid duplicate traversal for single column
                for row in range(bottom - 1, top, -1):
                    result.append(matrix[row][left])

            # Recursively traverse inner matrix
            result += spiral_helper(matrix, top + 1, bottom - 1, left + 1, right - 1)

            return result

        return spiral_helper(matrix, 0, len(matrix) - 1, 0, len(matrix[0]) - 1)
        