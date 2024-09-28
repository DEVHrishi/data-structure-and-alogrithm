'''Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2'''

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        prefix_sum = 0
        count = 0
        for i in nums:
            prefix_sum += i
            
            if prefix_sum - k in d:
                count += d[prefix_sum - k]
            d[prefix_sum] += 1
        return count