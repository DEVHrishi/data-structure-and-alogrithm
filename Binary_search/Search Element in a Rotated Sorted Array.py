def search_rotated_sorted_array(nums, target):
    n = len(nums)
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        # If left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # If right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
