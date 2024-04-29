def recursive_selection_sort(arr):
    if len(arr) <= 1:
        return arr

    # Find the minimum element in the remaining unsorted array
    min_index = arr.index(min(arr))
    
    # Swap the minimum element with the first element
    arr[0], arr[min_index] = arr[min_index], arr[0]
    
    # Recursively sort the remaining array
    recursive_selection_sort(arr[1:])
    
    return arr