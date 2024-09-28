# tc = O(log n) and sc = O(1)
def count_rotations(arr):
    n = len(arr)
    l, r = 0, n - 1
    
    # If the array is not rotated, return 0
    if arr[l] < arr[r]:
        return 0
    
    while l <= r:
        mid = (l + r) // 2
        next = (mid + 1) % n
        prev = (mid + n - 1) % n
        
        # If the middle element is smaller than both its neighbors, it is the smallest element
        if arr[mid] < arr[next] and arr[mid] < arr[prev]:
            return mid
        
        # If the left half is sorted, search in the right half
        elif arr[mid] >= arr[l]:
            l = mid + 1
        
        # If the right half is sorted, search in the left half
        else:
            r = mid - 1
