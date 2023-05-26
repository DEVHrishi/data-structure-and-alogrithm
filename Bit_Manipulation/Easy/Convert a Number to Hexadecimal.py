'''Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

 

Example 1:

Input: num = 26
Output: "1a"
Example 2:

Input: num = -1
Output: "ffffffff"'''

# tc = O(1) and sc = O(1)
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_digits = "0123456789abcdef"
        result = ""
        
        # 32-bit representation of num
        mask = (1 << 32) - 1
        num = num & mask
        
        while num > 0:
            # Extract the last 4 bits and convert to hex digit
            digit = hex_digits[num & 15]
            result = digit + result
            num >>= 4
        
        return result
