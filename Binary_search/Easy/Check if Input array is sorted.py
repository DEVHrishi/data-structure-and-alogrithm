def is_sorted(arr):
    n = len(arr)
    left, right = 0, n - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[mid + 1]:
            return False

        if arr[left] <= arr[mid]:
            left = mid + 1
        else:
            right = mid

    return True

# Example usage
arr = [1, 2, 3, 4, 5]
print(is_sorted(arr))  # Output: True

arr = [5, 4, 3, 2, 1]
print(is_sorted(arr))  # Output: False

arr = [1, 3, 2, 4, 5]
print(is_sorted(arr))  # Output: False
