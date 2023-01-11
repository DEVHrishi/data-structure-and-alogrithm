upper_bound = int(input('Enter a number: '))
lower_bound = int(input('Enter a number: '))

num = []

for i in range(lower_bound, upper_bound+1):
    n = len(str(i))
    sum = 0
    temp = i
    while temp > 0:
        x = temp % 10
        sum += x ** n
        temp //= 10

    if sum == i:
        num.append(i)

print(num)

    