from array import *

array_input = array('i', [1, 3, 5, 7, 9])

for i in array_input:
    print(i)

print("Access first three items individually")

for i in range(0, 3):
    print(array_input[i])
