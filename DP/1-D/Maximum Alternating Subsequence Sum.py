'''The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices minus the sum of the elements at odd indices.

For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
Given an array nums, return the maximum alternating sum of any subsequence of nums (after reindexing the elements of the subsequence).

A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2,4,2] is not.

 

Example 1:

Input: nums = [4,2,5,3]
Output: 7
Explanation: It is optimal to choose the subsequence [4,2,5] with alternating sum (4 + 5) - 2 = 7.
Example 2:

Input: nums = [5,6,7,8]
Output: 8
Explanation: It is optimal to choose the subsequence [8] with alternating sum 8.
Example 3:

Input: nums = [6,2,1,2,4,5]
Output: 10
Explanation: It is optimal to choose the subsequence [6,1,5] with alternating sum (6 + 5) - 1 = 10.'''

# top-down
# tc: O(n) and sc: O(n)
class Solution:
    def fun(self, nums, i, isEven, dp):
        if i >= len(nums):
            return 0
        if (i, isEven) in dp:
            return dp[(i, isEven)]
        
        skip = self.fun(nums, i + 1, isEven, dp)
        val = nums[i]
        if not isEven:
            val = -val
        pick = val + self.fun(nums, i + 1, not isEven, dp)

        dp[(i, isEven)] = max(pick, skip)
        return dp[(i, isEven)]

    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        return self.fun(nums, 0, True, dp)

# bottom-up
# tc: O(n) and sc: O(n)
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # Initialize dp arrays
        even = [0] * n  # dp[i][0]
        odd = [0] * n   # dp[i][1]
        
        even[0] = nums[0]
        odd[0] = 0
        
        for i in range(1, n):
            even[i] = max(even[i-1], odd[i-1] + nums[i])
            odd[i] = max(odd[i-1], even[i-1] - nums[i])
        
        return max(even[-1], odd[-1])