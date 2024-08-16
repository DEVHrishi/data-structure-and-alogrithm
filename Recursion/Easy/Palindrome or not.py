def palindrome(s, n, i):
    if s[i] != s[-i-1]:
        return False
    elif i == n//2:
        return True
    else:
        return palindrome(s, n, i+1)

s = 'aaaaaaa'
n = len(s)
i=0
print(palindrome(s,n,i))