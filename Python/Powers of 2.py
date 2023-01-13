n = int(input('Enter a number: '))
num = []
x = lambda i: 2 ** i
for i in range(n):
    j = x(i)
    num.append(j)

print(num)