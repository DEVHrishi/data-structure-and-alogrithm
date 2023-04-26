def findMinDiffElement(arr, target):
    n = len(arr)
    if target <= arr[0]:
        return arr[0]
    elif target >= arr[n-1]:
        return arr[n-1]
    else:
        l, r = 0, n-1
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] == target:
                return arr[mid]
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        # l is now the index where target should be inserted
        diff_left = abs(arr[l-1] - target)
        diff_right = abs(arr[l] - target)
        if diff_left <= diff_right:
            return arr[l-1]
        else:
            return arr[l]
