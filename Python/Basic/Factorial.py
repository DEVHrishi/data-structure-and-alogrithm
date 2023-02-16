n = int(input('Enter a number: '))
x=1
if n== 0 or n==1:
    print('factorial of n: 1')
else:
    for i in range(1,n+1):
        x = x*i
print(x)

def factorial(n):
    if n== 0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
num = factorial(n)
print(num)