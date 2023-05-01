'''You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.

Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

Example 1:

Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
Example 2:

Input: coordinates = "h3"
Output: true
Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.
Example 3:

Input: coordinates = "c7"
Output: false'''

# tc and sc = O(1)
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        k = d.index(coordinates[0])
        if (k + int(coordinates[1])) % 2 == 0:
            return True
        else:
            return False
        
class Solution:
    def squareIsWhite(self, c: str) -> bool:
        return (ord(c[0])+int(c[1]))%2