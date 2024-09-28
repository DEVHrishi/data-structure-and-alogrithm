'''Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.'''


from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = defaultdict(int)
        d[0] = -1
        prefix_sum = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1
            if prefix_sum in d:
                count = max(count, i-d[prefix_sum])
            else:
                d[prefix_sum] = i
            # print(i, prefix_sum, count , d)
        return count
