'''Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]'''

# tc: o(m*n) and sc: o(m*n)
class Solution:
    from collections import defaultdict
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dict = defaultdict(list)
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                key = (row+col)
                dict[key].append(mat[row][col])
        print(dict)
        result = []
        for key, value in dict.items():
            if key % 2 == 0:
                result += value[::-1]
            else:
                result += value
        return result
        
# tc: o(m*n) and sc: o(1)
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        row = col = 0
        for i in range(len(mat)*len(mat[0])):
            print(row, col)
            result.append(mat[row][col])

            if (row+col) % 2 == 0:
                if col == len(mat[0]) - 1:
                    row += 1
                elif row == 0:
                    
                    col += 1
                else:
                    row  -= 1
                    col += 1
            else:
                if row == len(mat) - 1:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1
        return result
    
# tc: o(m*n) and sc: o(1)
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def recursiveHelper(row, col, direction, result):
            # Base case: If the current indices are out of the matrix bounds
            if row >= len(mat) or col >= len(mat[0]):
                return

            result.append(mat[row][col])

            # Calculate next position based on the current direction
            if direction == 'up':
                if col == len(mat[0]) - 1:  # Hit the right boundary
                    recursiveHelper(row + 1, col, 'down', result)
                elif row == 0:  # Hit the top boundary
                    recursiveHelper(row, col + 1, 'down', result)
                else:
                    recursiveHelper(row - 1, col + 1, 'up', result)
            else:  # direction == 'down'
                if row == len(mat) - 1:  # Hit the bottom boundary
                    recursiveHelper(row, col + 1, 'up', result)
                elif col == 0:  # Hit the left boundary
                    recursiveHelper(row + 1, col, 'up', result)
                else:
                    recursiveHelper(row + 1, col - 1, 'down', result)

        result = []
        if mat:
            recursiveHelper(0, 0, 'up', result)
        return result