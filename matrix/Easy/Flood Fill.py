'''An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

 

Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.'''

# tc: O(m*n) and sc: o(m*n)
class Solution:
    def dfs(self, image, sr, sc, color, prev):
        # Boundary conditions
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return
        # If the current cell is not the previous color or already the new color, return
        if image[sr][sc] != prev or image[sr][sc] == color:
            return
        
        # Update the color
        image[sr][sc] = color
        
        # Recursively call dfs in all 4 directions
        self.dfs(image, sr, sc+1, color, prev)
        self.dfs(image, sr, sc-1, color, prev)
        self.dfs(image, sr+1, sc, color, prev)
        self.dfs(image, sr-1, sc, color, prev)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] != color:
            self.dfs(image, sr, sc, color, image[sr][sc])
        return image

from collections import deque
# tc: O(m*n) and sc: o(m*n)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Get the initial color
        start_color = image[sr][sc]

        # If the start color is the same as the target color, return the original image
        if start_color == color:
            return image

        # Initialize a queue for BFS
        queue = deque([(sr, sc)])
        image[sr][sc] = color

        # Define directions for moving in 4-connected directions (right, left, down, up)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            current_row, current_col = queue.popleft()

            # Explore neighbors
            for direction in directions:
                new_row = current_row + direction[0]
                new_col = current_col + direction[1]

                # Check if the new position is within bounds and has the start color
                if 0 <= new_row < len(image) and 0 <= new_col < len(image[0]) and image[new_row][new_col] == start_color:
                    image[new_row][new_col] = color
                    queue.append((new_row, new_col))

        return image
