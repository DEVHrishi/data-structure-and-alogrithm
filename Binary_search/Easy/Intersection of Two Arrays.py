'''Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.'''

from ast import List

# tc = O(n+m) and sc = O(n+m)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2))

# tc = O((m + n) log m) and sc = O(1)
class Solution:
    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []

        for num in nums1:
            if self.binary_search(nums2, num) and num not in result:
                result.append(num)

        return result

# tc = O(n+m) and sc = O(k), k is size of result
def twoPointerSol(self, numOne, numTwo):
        numOne.sort()
        numTwo.sort()

        left, right = 0, 0
        result = []
        while left < len(numOne) and right < len(numTwo):
            if numOne[left] < numTwo[right]:
                left += 1
            elif numTwo[right] < numOne[left]:
                right += 1
            else:
                result.append(numOne[left])
                right += 1
                left += 1

            
        return list(set(result))