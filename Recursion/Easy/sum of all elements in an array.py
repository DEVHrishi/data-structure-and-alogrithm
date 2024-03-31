
def array_sum(l, n):
    if n == 0:
        return 0
    else:
        return l[n-1] + array_sum(l, n-1)

l = [1, 2, 4, 6, 8, 4]
n = len(l)
print(array_sum(l, n))