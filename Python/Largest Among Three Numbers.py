a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
c = int(input('Enter a number: '))

if a>b and a>c:
    print('a is largest')
elif b>a and b>c:
    print('b is largest')
else:
    print('c is largest')