def binary_search_nearly_sorted(arr, target):
    n = len(arr)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        if mid > 0 and arr[mid-1] == target:
            return mid - 1
        if mid < n-1 and arr[mid+1] == target:
            return mid + 1
        if arr[mid] > target:
            r = mid - 2
        else:
            l = mid + 2
    return -1
