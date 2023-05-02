def findPeakElement(nums):
    n = len(nums)
    l, r = 0, n-1
    while l <= r:
        m = (l + r) // 2
        if (m == 0 or nums[m-1] <= nums[m]) and (m == n-1 or nums[m] >= nums[m+1]):
            return m
        elif m > 0 and nums[m-1] > nums[m]:
            r = m - 1
        else:
            l = m + 1
    return -1


arr = [ 1, 3, 20, 4, 1, 0 ]
print(findPeakElement(arr))