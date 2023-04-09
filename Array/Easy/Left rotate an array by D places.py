# tc = O(n+d) and sc = O(d)
def left_rotate(arr, d):
    n = len(arr)
    temp = [0] * d
    
    # store the first d elements in a temporary array
    for i in range(d):
        temp[i] = arr[i]
        
    # shift the remaining elements d positions to the left
    for i in range(d, n):
        arr[i-d] = arr[i]
        
    # copy the d elements from the temporary array to the end of the original array
    for i in range(d):
        arr[n-d+i] = temp[i]
        
    return arr

arr = [1, 2, 3, 4, 5]
d = 2
print(left_rotate(arr, d))  # Output: [3, 4, 5, 1, 2]

'''2nd method'''
# tc = O(n) and sc = O(1)
def reverse_array(arr, start, end):
    # reverse the elements of the array between start and end indices
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_rotate(arr, d):
    n = len(arr)
    
    # reverse the first d elements of the array
    reverse_array(arr, 0, d-1)
    
    # reverse the remaining elements of the array
    reverse_array(arr, d, n-1)
    
    # reverse the entire array
    reverse_array(arr, 0, n-1)
    
    return arr

