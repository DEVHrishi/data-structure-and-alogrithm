'''You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1'''

from ast import List
from bisect import insort_left
import heapq

# tc: O(n^2) and sc: O(1)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while stones:
            s1 = stones.pop()  # the heaviest stone
            if not stones:  # s1 is the remaining stone
                return s1
            s2 = stones.pop()  # the second-heaviest stone; s2 <= s1
            if s1 > s2:
                # the remaining stone will be s1-s2
                # loop through stones to find the index to insert the stone
                for i in range(len(stones)+1):
                    if i == len(stones) or stones[i] >= s1-s2:
                        stones.insert(i, s1-s2)
                        break
            # else s1 == s2; both stones are destroyed
        return 0  # if no more stones remaining

# tc: O(n^2) and sc: O(1)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while stones:
            s1 = stones.pop()  # the heaviest stone
            if not stones:  # s1 is the remaining stone
                return s1
            s2 = stones.pop()  # the second-heaviest stone; s2 <= s1
            if s1 > s2:
                # the remaining stone will be s1-s2
                # binary-insert the remaining stone into stones
                insort_left(stones, s1-s2)
            # else s1 == s2; both stones are destroyed
        return 0  # if no more stones remain
    
# tc: O(n log n) and sc: O(n)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-val for val in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            if (diff := -1*heapq.heappop(heap) + heapq.heappop(heap)):
                heapq.heappush(heap, -diff)
        return 0 if not heap else (-1 * heap[0])
    
