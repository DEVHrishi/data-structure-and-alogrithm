s = 'abcd'
def reverse_str(s):
    if len(s) == 0:
        return ''
    else:
        return s[-1]+reverse_str(s[:-1])
print(reverse_str(s))