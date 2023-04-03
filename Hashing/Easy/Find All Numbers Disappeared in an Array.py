'''Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]'''

from ast import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr=set(nums)
        a,n=[],len(nums)
        for i in range(1,n+1):
            if i not in arr:
                a.append(i)
        return a
    
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            nums[abs(i) - 1]  = -abs(nums[abs(i) - 1])
            
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]