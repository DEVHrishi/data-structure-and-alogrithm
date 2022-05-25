from array import *
arr_input = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
a = int(input('Enter a number: '))
z = arr_input.count(a)
if z > 1:
    print('True')
else:
    print('False')
