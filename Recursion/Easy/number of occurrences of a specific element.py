l = [1, 3, 4, 1, 8]
c = 0
def occur(l, n, c, x):
    if n == -1:
        return c
    else:
        if l[n] == x:
            c += 1
        return occur(l, n-1, c, x)
print(occur(l, len(l)-1, c, 4))


def occur(l, x):
    if not l: # if the list is empty, return 0
        return 0
    else:
        return (l[0] == x) + occur(l[1:], x) # add 1 if the first element is x, then check the rest of the list

l = [1, 3, 4, 1, 8]
print(occur(l, 4))