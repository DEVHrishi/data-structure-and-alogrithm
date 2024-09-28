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
