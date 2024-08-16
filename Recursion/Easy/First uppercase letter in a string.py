'''Given a string find its first uppercase letter
Examples : 

Input : geeksforgeeKs
Output : K

Input  : geekS
Output : S'''

def fun(s):
    if len(s) < 1:
        return -1
    if s[0].isupper():
        return s[0]
    return fun(s[1:])

ans = fun('abCeF')
print(ans)