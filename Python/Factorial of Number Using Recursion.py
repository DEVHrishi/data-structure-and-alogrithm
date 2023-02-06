# tc= O(n)

def factorial(n):
    if n <= 1:
        return n
    else: 
        return n * factorial(n-1)

num = int(input('Enter a number: '))

if num <= 0:
    print('Enter a positive number')
else:
    print('factorial of a number: ', factorial(num))