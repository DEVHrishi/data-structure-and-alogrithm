'''
Input: A * B + C / D
Output: + * A B/ C D '''


def InfixtoPrefix(exp):
    #code here
    operators = set(['+', '-', '*', '/', '(', ')', '^'])
    power = {'-':1, '+':1, '/':2, '*':2, '^':3}
    stack = []
    ans = ""
    
    for i in exp[::-1]:
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
    return ans[::-1]

x = 'A * B + C / D'
print(InfixtoPrefix(x))