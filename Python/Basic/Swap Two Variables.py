
a = int(input('Enter a number: '))
b = int(input('Enter a number: '))

a, b = b, a
'''temp =  a
a = b
b = temp'''

print ('a = {} and b = {}'.format(a,b))
