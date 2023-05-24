'''Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

Example 1:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101
Example 2:

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
Example 3:

Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.'''

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n:
            bit1 = n & 1
            n = n >> 1
            bit2 = n & 1
            if bit1 == bit2:
                return False
        return True