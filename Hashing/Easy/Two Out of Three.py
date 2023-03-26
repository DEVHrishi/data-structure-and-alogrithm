'''Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.
 

Example 1:

Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]
Explanation: The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.
Example 2:

Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
Output: [2,3,1]
Explanation: The values that are present in at least two arrays are:
- 2, in nums2 and nums3.
- 3, in nums1 and nums2.
- 1, in nums1 and nums3.
Example 3:

Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
Output: []
Explanation: No value is present in at least two arrays.'''

from ast import List
from collections import Counter


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        l = []
        for i in nums1:
            if i in nums2:
                l.append(i)
            if i in nums3:
                l.append(i)
        for j in nums2:
            if j in nums3:
                l.append(j)
        return list(set(l))
    
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int] :
        return list(set(list(set(nums1) & set(nums2)) + list(set(nums2) & set(nums3)) + list(set(nums3) & set(nums1))))
    
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        freq = Counter()
        for nums in nums1, nums2, nums3: freq.update(set(nums))
        return [k for k, v in freq.items() if v >= 2]