'''Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.'''

# tc: o(n) and sc: O(1)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        i,j = 0, 0
        zeros = 0
        while j < len(nums):
            if nums[j] == 0:
                zeros += 1
            while zeros > k:
                if nums[i] == 0:
                    zeros -= 1
                i += 1
            
            count = max(count , j - i + 1)
            j += 1
        return count