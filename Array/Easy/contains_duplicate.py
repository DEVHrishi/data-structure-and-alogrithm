def duplicate(arr_input):
    arr_input.sort()
    for i in range(len(arr_input)):
        if arr_input[i] == arr_input[i+1]:
            return True
        else:
            return False
    

print('duplicate contains:',duplicate([1,2,3,5,7,9,10]))