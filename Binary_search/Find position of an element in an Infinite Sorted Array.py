def binary_search(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def find_position(arr, target):
    if arr[0] == target:
        return 0

    # Find the range in which the target element exists
    i = 1
    while i < len(arr) and arr[i] < target:
        i *= 2

    # Perform binary search within the range to find the exact position of the element
    return binary_search(arr, i // 2, min(i, len(arr) - 1), target)
