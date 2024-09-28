# tc = O(log n)
def binary_search_first_last(arr, x):
    # Find first occurrence
    first = None
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            first = mid
            r = mid - 1
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    
    # Find last occurrence
    last = None
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            last = mid
            l = mid + 1
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    
    return (first, last)
