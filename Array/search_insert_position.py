def search(arr_input, target):
    for i in range(len(arr_input)):
        if arr_input[i] == target:
            return i
        if arr_input[i] > target:
            return i

print('search insert position:', search([1,3,5,6], 2))