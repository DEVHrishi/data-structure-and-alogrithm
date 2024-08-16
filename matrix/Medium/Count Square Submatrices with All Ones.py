'''Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.'''

# tc: O(m*n) and sc: o(m*n)
class Solution:
    def dfs(self, matrix, row, col, memo):
        # boundary conditions
        if row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] == 0:
            return 0
        # check if memorized 
        if memo[row][col] != -1:
            return memo[row][col]
        
        # traverse right, down, diag
        right = self.dfs(matrix, row, col + 1, memo)
        down = self.dfs(matrix, row+ 1, col, memo)
        diag = self.dfs(matrix, row+1, col+1, memo)

        memo[row][col] = 1 + min(right, down, diag)
        return memo[row][col]
        
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        memo = [[-1]*len(matrix[0]) for _ in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                ans += self.dfs(matrix, row, col, memo)
        return ans
    
# tc: O(m*n) and sc: o(1)
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 1:
                    matrix[row][col] = 1 + min(matrix[row][col-1], matrix[row-1][col], matrix[row-1][col-1])
        print(matrix)
        count = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] > 0:
                    count += matrix[row][col]
        return count