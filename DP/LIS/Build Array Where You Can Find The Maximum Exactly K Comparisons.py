'''You are given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:


You should build the array arr which has the following properties:

arr has exactly n integers.
1 <= arr[i] <= m where (0 <= i < n).
After applying the mentioned algorithm to arr, the value search_cost is equal to k.
Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.

 

Example 1:

Input: n = 2, m = 3, k = 1
Output: 6
Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
Example 2:

Input: n = 5, m = 2, k = 3
Output: 0
Explanation: There are no possible arrays that satisfy the mentioned conditions.
Example 3:

Input: n = 9, m = 1, k = 1
Output: 1
Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]'''

class Solution:
    def fun(self, idx, cost, prev_max, n, m, k, memo):
        """
        Dynamic programming solution to count arrays with specific search cost
        
        Parameters:
        idx: current position in array
        cost: current search cost (number of new maximums seen)
        prev_max: previous maximum value seen
        n: target array length
        m: maximum allowed value
        k: target search cost
        memo: memoization array
        """
        # If we've filled all positions
        if idx == n:
            # Valid array if cost equals target k
            return 1 if cost == k else 0
            
        # Return memoized result if available
        if memo[idx][cost][prev_max] != -1:
            return memo[idx][cost][prev_max]
        
        result = 0
        MOD = 10**9 + 7
        
        # Try all possible values from 1 to m at current position
        for curr_val in range(1, m + 1):
            # If current value is greater than previous maximum,
            # it contributes to search cost
            if curr_val > prev_max:
                # Only proceed if we haven't exceeded target cost
                if cost + 1 <= k:
                    result = (result + self.fun(idx + 1, cost + 1, 
                            curr_val, n, m, k, memo)) % MOD
            else:
                # Current value doesn't create new maximum
                result = (result + self.fun(idx + 1, cost, 
                        prev_max, n, m, k, memo)) % MOD
        
        memo[idx][cost][prev_max] = result
        return result

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # Invalid cases:
        # 1. k = 0 is impossible as we must have at least one maximum
        # 2. k > m is impossible as we can't have more new maximums than distinct values
        # 3. k > n is impossible as we can't have more new maximums than array length
        if k == 0 or k > min(m, n):
            return 0
            
        # Create 3D memoization array
        # dimensions: position × cost × previous maximum
        memo = [[[-1] * (m + 1) for _ in range(k + 1)] for _ in range(n)]
        
        # Start with position 0, cost 0, and previous maximum 0
        return self.fun(0, 0, 0, n, m, k, memo)