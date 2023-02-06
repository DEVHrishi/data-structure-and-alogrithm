# tc= O(n)

def sum_natural(n):
    if n <= 1:
        return n
    else: 
        return n + sum_natural(n-1)

num = int(input('Enter a number: '))

if num <= 0:
    print('Enter a positive number')
else:
    print('Sum of natural number: ', sum_natural(num))