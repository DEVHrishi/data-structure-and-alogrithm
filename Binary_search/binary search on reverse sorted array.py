def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x: 
            l = mid + 1  
        else:
            r = mid - 1
    return -1

arr = [7, 6, 5, 4, 3, 1]
l, r = 0, len(arr)-1
x = 6
print(binarySearch(arr, l, r, x))
