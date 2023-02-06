# tc=O(2^n)

def fib_rec(n):
    if n <= 1:
        return n
    else:
        return (fib_rec(n-1) + fib_rec(n-2))

num = int(input('Enter a number: '))

if num < 1: 
    print('Enter a positive number')
else:
    print('Fibonacci sequence: ')
    for i in range(num):
        print(fib_rec(i))
