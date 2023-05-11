'''A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

 

Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".'''

# tc = O(n) and sc = O(n)
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans, cnt = [], 0
        for ch in s:
            if ch == '(' and cnt > 0: ans.append(ch)
            if ch == ')' and cnt > 1: ans.append(ch)
            cnt += 1 if ch == '(' else -1
        return "".join(ans)
    
# tc = O(n) and sc = O(n)
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        i=j=1
        n = len(s)
        opening_count = 1
        closing_count = 0
        result = ""
        while j<n: 
            if  opening_count != closing_count:
                if s[j] == "(":
                    opening_count +=1
                else:
                    closing_count +=1
                j +=1
                if j ==n and  opening_count == closing_count :
                    result += s[i:j-1]
            else:
                result += s[i:j-1]
                j += 1
                i = j
                opening_count = 1
                closing_count = 0
        return result