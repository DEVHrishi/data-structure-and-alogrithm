'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false'''

# tc = O(n) and sc = O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            
            elif stack and ((i == ')' and stack[-1] == '(') or (i == '}' and stack[-1] == '{') or (i == ']' and stack[-1] == '[')):
                    stack.pop()
            else:
                stack.append(i)
        return False if stack else True