'''Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for k in range(len(nums)):
            i = k + 1
            j = len(nums) - 1

            while i < j:
                sm = nums[i] + nums[j] + nums[k]
                if abs(target - sm) < abs(target - closest):
                    closest = sm
                if sm > target:
                    j -= 1
                else:
                    i += 1
        return closest