'''Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

Example 1:

Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
Example 2:

Input: nums = [1,2,1,10]
Output: 0
Explanation: 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.'''

from ast import List

# tc: O(nlogn) and sc: O(1)
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int: # nums = [3,6,2,3]
        # condition to create a triangle a < (b + c). where  a >= b >= c
        nums = sorted(nums, reverse=True) # nums after sorting = [6, 3, 3, 2]
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] +nums[i+2]: # When i =1 => 3 < 3+2 (True)
                return nums[i]+nums[i+1] +nums[i+2] # 3 + 3 + 2 = 8
        return 0