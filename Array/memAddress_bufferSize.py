from array import *
arr_input = array('i', [1,3,5,7,9])
print('Original array: '+str(arr_input))
print('Current memory address and the length in elements of the buffer: '+str(arr_input.buffer_info()))
print('The size of the memory buffer in bytes: '+str(arr_input.buffer_info()[1]*arr_input.itemsize))