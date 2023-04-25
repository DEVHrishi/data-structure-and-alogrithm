def find_first_one(arr):
    low, high = 0, 1

    while arr[high] == 0:
        low = high
        high *= 2

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == 1 and (mid == 0 or arr[mid - 1] == 0):
            return mid
        elif arr[mid] == 1:
            high = mid - 1
        else:
            low = mid + 1

    return -1
