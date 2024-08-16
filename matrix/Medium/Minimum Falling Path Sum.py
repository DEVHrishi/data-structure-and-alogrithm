'''Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

Example 1:


Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
Example 2:


Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.'''

# tc: O(m*n) and sc: o(1)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] += min(matrix[row-1][col-1] if col > 0 else float('inf'), matrix[row-1][col], matrix[row-1][col+1] if col < len(matrix[0])-1 else float('inf'))
        return min(matrix[-1])

# tc: O(m*n) and sc: o(m*n) time limit exceed
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[-1 for i in range(n)] for i in range(n)]
        def helper(i, j):

            if j < 0 or j >= n:
                return float('inf')

            if i == n-1:
                return matrix[n-1][j]

            if dp[i][j] != -1:
                return dp[i][j]

            down = matrix[i][j] + helper(i+1, j)
            ld = matrix[i][j] + helper(i+1, j - 1)
            rd = matrix[i][j] + helper(i+1, j+1)

            dp[i][j] = min(down, ld, rd)
            return dp[i][j]

        ans = float('inf')
        for j in range(n):
            ans = min(ans, helper(0, j))

        return ans

# tc: O(m*n) and sc: o(m*n) accepted
class Solution:

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)

        @cache
        def dfs(x, y):
            if x < 0 or x >= n: return inf
            if y == n: return 0
            left = dfs(x - 1, y + 1)
            down = dfs(x, y + 1)
            right = dfs(x + 1, y + 1)
            return matrix[y][x] + min(left, down, right)

        ans = inf
        for x in range(n):
            ans = min(ans, dfs(x, 0))

        return ans