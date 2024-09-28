'''Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

 

Example 1:

Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
Example 2:

Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
Example 3:

Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.'''

from ast import List

# tc = O(n log n) and sc = O(1)
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        first_pos = self.find_first_positive(nums)
        last_neg = self.find_last_negative(nums)
        return max(last_neg + 1, len(nums) - first_pos)

    def find_first_positive(self, nums):
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > 0:
                right = mid
            else:
                left = mid + 1
        return left
    
    def find_last_negative(self, nums):
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= 0:
                right = mid
            else:
                left = mid + 1
        return left - 1


# tc = O(n log n) and sc = O(n)
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0]==nums[-1]==0:
            return 0
        n = len(nums)
        l,r = 0, n
        while l<r:
            m = (l+r)//2
            if nums[m]<0:
                l = m+1
            else:
                r = m
        
        if l==n:
            return n
        if nums[l]==0:
            return max(l, n-l-1)
        return max(l, n-l)