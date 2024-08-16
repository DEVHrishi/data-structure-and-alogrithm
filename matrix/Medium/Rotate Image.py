'''You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]'''

# tc: o(n^2) and sc: o(1) // if we neglect the recursive stack space
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix)-1

        while l < r:
            for i in range(r-l):
                top, buttom = l, r
                top_left = matrix[top][l+i]
                matrix[top][l+i] = matrix[buttom-i][l]
                matrix[buttom-i][l] = matrix[buttom][r-i]
                matrix[buttom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = top_left
            r -= 1
            l += 1
        return matrix

# tc: o(n^2) and sc: o(1)
class Solution:
    def helper(self, matrix, left, right):
        if left >= right:
            return
        for i in range(right - left):
            top, buttom = left, right
            top_left = matrix[top][left+i]
            matrix[top][left+i] = matrix[buttom-i][left]
            matrix[buttom-i][left] = matrix[buttom][right-i]
            matrix[buttom][right-i] = matrix[top+i][right]
            matrix[top+i][right] = top_left
        self.helper(matrix, left+1, right-1)
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.helper(matrix, 0, len(matrix)-1)
        return matrix