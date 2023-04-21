from ast import List

# tc = O(log n) and sc = O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot index
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l
        
        # determine which subarray to search
        if target >= nums[0]:
            l, r = 0, pivot-1
        else:
            l, r = pivot, n-1
        
        # perform binary search on the appropriate subarray
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1
