'''Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.'''

from ast import List
from collections import Counter

# binary search
# tc = O(n log n + len(nums1) * log len(nums2)) and sc = O(min(len(nums1), len(nums2)))
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for val in nums1:
            res,pos = self.search(val,nums2)
            if res == True:
                del nums2[pos]
                result.append(val)
        return result
    
def search(self,val,a):
    a.sort()
    l = 0
    h = len(a)-1 
    while l <= h:
        mid = (l + h) // 2
        if a[mid] == val:
            return True,mid
        elif a[mid] < val:
            l = mid + 1
        else:
            h = mid - 1
    return False,-1


# two pointer approach
# tc = O(nlogn) and sc = O(min(len(nums1), len(nums2)))
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []
        i,j=0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        return result
    
# tc = O(M + N) and sc = O(min(M, N))
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)
            
        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans