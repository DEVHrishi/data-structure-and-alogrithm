class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1

        while left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
class Solution:
    def binary_search(self, i, j, nums, target):
        if i <= j:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.binary_search(mid+1, j, nums, target)
            else:
                return self.binary_search(i, mid-1, nums, target)
        else:
            return -1
    def search(self, nums: List[int], target: int) -> int:
        i,j = 0, len(nums) - 1
        return self.binary_search(i,j,nums, target)