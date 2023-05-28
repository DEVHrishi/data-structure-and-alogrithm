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
        arr=['2']
        for i in s:
            if i =="(" or i=='[' or i=='{':
          
                arr.append(i)
            elif (i =="]" and arr[-1]=="[") or (i==')' and arr[-1]=='(') or (i=='}' and arr[-1]=='{'):
                arr.pop()
            else:
                return False
                break
        if len(arr)==1:
            return True
        else:
            return False 