def binarySearch(arr, l, r, x):
    mid = l + (r - l) // 2
    while l <= r:
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

arr = [1, 2, 4, 5, 7]
l, r = 0, len(arr)-1
x = 4
print(binarySearch(arr, l, r, x))