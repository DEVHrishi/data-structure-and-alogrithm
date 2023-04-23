def next_alpha(arr, x):
    n = len(arr)
    res = None
    l, r = 0, n-1
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] < x:
            l = mid + 1
        else:
            res = arr[mid]
            r = mid - 1
    return res
