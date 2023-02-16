# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.

num = int(input('Enter a number: '))
order = len(str(num))
x = 0

temp = num

while temp > 0:
    n = temp % 10
    x += n**order
    temp //= 10

if x == num:
    print('number is armstrong number')
else:
    print('number is not armstrong number')