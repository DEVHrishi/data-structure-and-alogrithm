def add(x, y):
    if x == 0:
        return 0
    else:
        return y + add(x-1, y)
print(add(2,8))

s = 'ab'
s= s.lower()