#tc = O(n * log(sum of array elements)) and sc = O(1)

def allocate_min_pages(arr, m):
    n = len(arr)
    if n < m:
        return -1
    max_pages = sum(arr)
    min_pages = max(arr)
    l, r = min_pages, max_pages
    result = float('inf')
    while l <= r:
        mid = (l + r) // 2
        if is_valid(arr, n, m, mid):
            result = mid
            r = mid - 1
        else:
            l = mid + 1
    return result

def is_valid(arr, n, m, mid):
    students = 1
    pages_allocated = 0
    for i in range(n):
        if arr[i] > mid:
            return False
        if pages_allocated + arr[i] > mid:
            students += 1
            pages_allocated = arr[i]
            if students > m:
                return False
        else:
            pages_allocated += arr[i]
    return True
