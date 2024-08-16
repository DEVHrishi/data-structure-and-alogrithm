'''You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false'''

# tc: O(log(m×n)) and sc: O(1)
class Solution:
    def search(self, matrix, left, right, target):
        if left > right:
            return False
        
        mid = (left+right)//2
        row, col = mid//len(matrix[0]), mid%len(matrix[0])
        
        if matrix[row][col] == target:
            return True
        if matrix[row][col] > target:
            return self.search(matrix, left, mid-1, target)
        else:
            return self.search(matrix, mid+1, right, target)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # calculate row an column length
        m = len(matrix)
        n = len(matrix[0])

        return self.search(matrix, 0, m*n-1, target)

# tc: O(log(m×n)) and sc: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False