'''You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.
Example 2:

Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.
Example 3:

Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.'''

from ast import List

# tc = O(n log n) and sc = O(1)
def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Sort the array in non-decreasing order
        nums.sort()
        
        # Perform binary search to find the target index
        target_index = binary_search(nums, target)
        
        # If the target element is not found, return an empty list
        if target_index == -1:
            return []
        
        # Expand the search to both sides of the target index to find all occurrences of the target element
        left, right = target_index, target_index
        while left >= 0 and nums[left] == target:
            left -= 1
            
        while right < len(nums) and nums[right] == target:
            right += 1
            
        return list(range(left + 1, right))