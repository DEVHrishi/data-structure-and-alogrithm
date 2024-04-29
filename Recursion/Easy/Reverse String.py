'''Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]'''

class Solution:
    def rev_str(self, s , l, r):
        if l > r:
            return s
        s[l], s[r] = s[r], s[l]
        return self.rev_str(s, l+1, r-1)

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.rev_str(s, 0, len(s)-1)