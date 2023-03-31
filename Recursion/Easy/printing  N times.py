def func(string, n):
    if n == 0:
        return
    else:
        print(string)
        func(string, n-1)
func('Hello World', 5)

