'''Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
 

Example 1:

Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]'''

# tc: o(n^2) and sc: o(1) // if we neglect the recursive stack space
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]
        print(image)
        for j in range(len(image)):
            for k in range(len(image[0])):
                image[j][k] = 1 - image[j][k]
        return image

# tc: o(n^2) and sc: o(1) // if we neglect the recursive stack space
class Solution:
    def helper(self, image, row, col, size):
        if row > size:
            return 
        
        if col > size//2:
            print("yes")
            self.helper(image, row+1, 0, size)
            return
        image[row][col], image[row][size-col] = 1 - image[row][size-col], 1 - image[row][col]
        self.helper(image, row, col+1, size)
        
            
        
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        self.helper(image, 0, 0, len(image)-1)
        return image