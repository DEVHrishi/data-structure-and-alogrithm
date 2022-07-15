def min_max (low, high, arr):
    max_arr = arr[low]
    min_arr = arr[low]

    if low == high:
        max_arr = arr[low]
        min_arr = arr[low]
        return (max_arr, min_arr)

    elif low == high - 1:
        if arr[low] > arr[high]:
            max_arr = arr[low]
            min_arr = arr[high]
        else:
            max_arr = arr[high]
            min_arr = arr[low]
        return (max_arr, min_arr)

    else:
        mid = (low + high) // 2
        max_arr1, min_arr1 = min_max(low, mid, arr)
        max_arr2, min_arr2 = min_max(mid+1, high, arr)

        return (max(max_arr1, max_arr2), min(min_arr1, min_arr2))

arr = [3, 5, 1, 9, 6, 7, 4, 2, 8]
arr_max, arr_min = min_max(0, len(arr)-1, arr)

print('Minimum element is ', arr_min)
print('Maximum element is ', arr_max)


