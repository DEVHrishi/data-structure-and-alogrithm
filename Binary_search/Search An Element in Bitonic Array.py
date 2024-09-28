def searchBitonicArray(arr, target):
    n = len(arr)
    
    # find the peak element
    left, right = 0, n - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    peak = left  # index of the peak element
    
    # search in the ascending subarray
    left, right = 0, peak
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # search in the descending subarray
    left, right = peak, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            right = mid - 1
        else:
            left = mid + 1
    
    # element not found
    return -1
