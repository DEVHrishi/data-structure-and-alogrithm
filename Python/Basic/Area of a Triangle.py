a = int(input('Enter a number1: '))
b = int(input('Enter a number2: '))
c = int(input('Enter a number3: '))

s = a + b + c

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print('Area of triangle : ', area)