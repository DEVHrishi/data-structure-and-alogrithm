def fun(n, i):
    if n <= 2:
        return True if n == 2 else False
    if n % i == 0:
        return False
    if (i * i) > n:
        return True
    return fun(n, i + 1)
print(fun(1, 2))