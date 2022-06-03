# brute force method tc = O(n^3) sc = O(1)
from cmath import inf


def maxSubArray(nums):
    ans = -inf
    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            ans = max(ans, cur_sum)
    return ans

# dynamic programming method tc = O(n) sc = O(n)


def maxSubArray(nums):
    dp = [*nums]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i-1])
    return max(dp)

# divide and conquer method tc = O(n) sc = O(n)


def maxSubArray(nums):
    pre, suf = [*nums], [*nums]
    for i in range(1, len(nums)):
        pre[i] += max(0, pre[i-1])
    for i in range(len(nums)-2, -1, -1):
        suf[i] += max(0, suf[i+1])

    def maxSubArray(A, L, R):
        if L == R:
            return A[L]
        mid = (L + R) // 2
        return max(maxSubArray(A, L, mid), maxSubArray(A, mid+1, R), pre[mid] + suf[mid+1])
    return maxSubArray(nums, 0, len(nums)-1)

# Kadane's Algorithm tc = O(n) sc = O(1) efficient approach


def maxSubArray(nums):
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)
