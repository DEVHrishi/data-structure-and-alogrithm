'''You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].'''

from ast import List
from collections import defaultdict
import heapq

# tc = O(n log n) and sc = O(n)
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        d = defaultdict(int)
        place = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        n = len(nums)
        a = [" "]*n
        for i in range(n): d[nums[i]] = i
        nums.sort(reverse=True)

        for i in range(n):
            if i < 3:
                a[d[nums[i]]] = place[i]            
            else:
                a[d[nums[i]]] = str(i+1)
                
        return a
    
# tc = O(n log n) and sc = O(n)
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        heapq.heapify(heap)
        result = [""]*len(score)
        for index in range(len(score)):
            heapq.heappush(heap,[-1*score[index],index])
        counter = 1
        while heap:
            index = heapq.heappop(heap)[1]
            if counter == 1:
                result[index] = "Gold Medal"
            elif counter == 2:
                result[index] = "Silver Medal"
            elif counter == 3:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(counter)
            counter += 1
        return result