'''Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"'''

def toLowerCase(self, s: str) -> str:
        return s.lower()

class Solution(object):
    def toLowerCase(self, s):
        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in s)