'''Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1'''

from ast import List
from collections import defaultdict

# tc: O(n^4) and sc: O(1)
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        c = 0
        for i in nums1:
            for j in nums2:
                for k in nums3:
                    for l in nums4:
                        if i + j + k + l == 0:
                            c += 1
        return c

# tc: O(n^2) and sc: O(n)
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n, hm, res = len(nums1), defaultdict(int), 0

        for i in range(n):
            for j in range(n):
                hm[nums1[i] + nums2[j]] += 1 

        for k in range(n):
            for l in range(n):
                res += hm[0 - (nums3[k] + nums4[l])]

        return res