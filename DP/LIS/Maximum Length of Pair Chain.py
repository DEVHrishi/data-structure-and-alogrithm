'''You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.

 

Example 1:

Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].
Example 2:

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].'''

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs = sorted(pairs, key = lambda x: x[1])
        dp = [1]*n

        for i in range(1, n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
    
class Solution:
    def fun(self, pairs, idx, prev, memo):
        if idx >= len(pairs):
            return 0
        if memo[prev][idx] != -1:
            return memo[prev][idx]
        pick = 0
        if prev == -1 or pairs[idx][0] > pairs[prev][1]:
            pick = 1 + self.fun(pairs, idx+1, idx, memo)
        skip = self.fun(pairs, idx+1, prev, memo)
        memo[prev][idx] = max(pick, skip)
        return memo[prev][idx]
        
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs = sorted(pairs, key = lambda x: x[1])
        memo = [[-1]*n for _ in range(n)]
        return self.fun(pairs, 0, -1, memo)