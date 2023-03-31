def func(n):
    if n == 0:
        return
    else:
        func(n-1)
        print(n)

func(5)