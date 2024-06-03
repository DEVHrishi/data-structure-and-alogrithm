'''Given a string S, The task is to remove all the consecutive duplicate characters of the string and return the resultant string. 

Examples: 

Input: S= “aaaaabbbbbb”
Output: ab

Input: S = “geeksforgeeks”
Output: geksforgeks

Input: S = “aabccba”
Output: abcba'''

def func(s, index, result):
    if index == len(s):
        return result
    if s[index] != s[index-1]:
        result += s[index]
    return func(s, index+1, result)

s = 'aaaabbb'
result = s[0]
print(func(s, 1, result))