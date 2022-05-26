# move all zero at the end of the array
def moveAllzero(arr, n):
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < n:
        arr[count] = 0
        count += 1
    return arr

arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
print(moveAllzero(arr, n))

# Time Complexity: O(n)
# Space Complexity: O(1)

# move all zero at the beginning of the array

def moveAllzero(arr, n):
    count = n-1
    i = n-1
    while i >= 0:
        if arr[i] != 0:
            arr[count] = arr[i]
            count -= 1
        i -= 1

    while count >= 0:
        arr[count] = 0
        count -= 1

    return arr


arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
print(moveAllzero(arr, n))  
        
