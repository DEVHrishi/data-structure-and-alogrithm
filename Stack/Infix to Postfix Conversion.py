'''
Input: str = "a+b*(c^d-e)^(f+g*h)-i"
Output: abcd^e-fgh*+^*+i-'''

# tc: O(n) and sc: O(n)
class Solution:
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        #code here
        operators = set(['+', '-', '*', '/', '(', ')', '^'])
        power = {'-':1, '+':1, '/':2, '*':2, '^':3}
        stack = []
        ans = ""
        
        for i in exp:
            if i not in operators:
                ans += i
            elif i == '(':
                stack.append("(")
            elif i == ')':
                while stack and stack[-1] != '(':
                    ans += stack.pop()
                stack.pop()
            else:
                while stack and stack[-1] != '(' and power[i] <= power[stack[-1]]:
                    ans += stack.pop()
                stack.append(i)
        while stack:
            ans += stack.pop()
        return ans
