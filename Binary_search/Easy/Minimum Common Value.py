'''Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.
Example 2:

Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.'''

from ast import List

# tc = O(mlogn) sc = O(1)
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for val in nums1:
            l, r = 0, len(nums2) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums2[mid] == val:
                    return val
                elif nums2[mid] < val:
                    l = mid + 1
                else:
                    r = mid - 1
        else:
            return -1


# tc = O(m+n) sc = O(1)
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1