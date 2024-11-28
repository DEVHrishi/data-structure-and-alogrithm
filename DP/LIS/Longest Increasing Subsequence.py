'''Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1'''


from typing import List

class Solution:
    def fun(self, nums, i, p, dp):
        if i >= len(nums):
            return 0
        if (p != -1 and dp[i][p] != -1):
            return dp[i][p]
        pick = 0
        if (p == -1 or nums[i] > nums[p]):
            pick = 1 + self.fun(nums, i+1, i, dp)
        skip = self.fun(nums, i+1, p, dp)

        dp[i][p] = max(pick, skip)
        return dp[i][p]

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1]*len(nums) for i in range(len(nums))]
        return self.fun(nums, 0, -1, dp)

# Example usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]
solution = Solution()
print(solution.lengthOfLIS(nums))



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)