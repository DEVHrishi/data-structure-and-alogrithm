'''You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

 

Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.'''

from ast import List

# tc = O(nlogn) and sc = O(n)
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        s = sorted(nums)
        for i in range(len(nums)-1):
            if s[i]*2 > s[-1]:
                return -1
        return nums.index(s[-1])

# tc = O(n) and sc = O(1)
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        for i in nums:
            if i != m and i*2 > m:
                return -1
        return nums.index(m)