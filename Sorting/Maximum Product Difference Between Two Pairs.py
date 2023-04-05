'''The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.

 

Example 1:

Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.
Example 2:

Input: nums = [4,2,5,9,7,4,8]
Output: 64
Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.'''

from ast import List

#O(nlogn) time O(1) space
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        s = sorted(nums, reverse = True)
        x = (s[0]*s[1]) - (s[-1]*s[-2])
        return x
    
#O(n) time O(1) space
def maxProductDifference(self, nums: List[int]) -> int:
        min1 = min2 = float('inf')
        max1 = max2 = float('-inf')
        for n in nums:
            if n <= min1:
                min1, min2, = n, min1
            elif n < min2:
                min2 = n
            if n >= max1:
                max1, max2 = n, max1
            elif n > max2:
                max2 = n
        return max1*max2-min1*min2