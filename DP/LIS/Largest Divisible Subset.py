'''Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]'''

from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n  # dp[i] will store the size of the largest subset ending at i
        prev = [-1] * n  # prev[i] will store the index of the previous element in the subset
        max_index = 0  # Index of the last element in the largest subset found

        # Build the dp array
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            # Track the largest subset's ending index
            if dp[i] > dp[max_index]:
                max_index = i

        # Reconstruct the largest divisible subset
        result = []
        while max_index >= 0:
            result.append(nums[max_index])
            max_index = prev[max_index]

        return result[::-1]  # Reverse to get the subset in the correct order


class Solution:
    def dfs(self, nums, idx, prev, temp, result, memo):
        if idx >= len(nums):
            if len(temp) > len(result[0]):
                result[0] = list(temp)
            return
        if memo[idx][prev] != -1:
            return memo[idx][prev]
        pick = 0
        if prev == -1 or (nums[idx] % nums[prev]) == 0:
            temp.append(nums[idx])
            memo[idx][prev] = self.dfs(nums, idx+1, idx, temp , result, memo)
            temp.pop()
        memo[idx][prev] = self.dfs(nums, idx+1, prev, temp, result, memo)

        
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        result = [[]]
        memo = [[-1]*n for _ in range(n)]
        self.dfs(nums, 0, -1, [], result, memo)
        return result[0]