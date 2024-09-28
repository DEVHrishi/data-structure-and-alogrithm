def ceil(arr, x):
    n = len(arr)
    l = 0
    r = n - 1
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] < x:
            l = mid + 1
        else:
            res = arr[mid]
            r = mid - 1
    return res
