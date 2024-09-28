def floor(arr, x):
    n = len(arr)
    l, r = 0, n-1
    res = -1
    while l <= r:
        mid = l + (r-l) // 2
        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] < x:
            res = arr[mid]
            l = mid + 1
        else:
            r = mid - 1
    return res
