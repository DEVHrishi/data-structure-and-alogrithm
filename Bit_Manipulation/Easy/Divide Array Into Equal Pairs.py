'''You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

 

Example 1:

Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
Example 2:

Input: nums = [1,2,3,4]
Output: false
Explanation: 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.'''

from ast import List

# tc = O(n log n) and sc = O(1)
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for i in set(nums):
            if nums.count(i) % 2 != 0:
                return False
        return True

# tc = O(n log n) and sc = O(1)
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums), 2):
            if nums[i] ^ nums[i+1] != 0:
                return False
        return True
    
# tc = O(n) and sc = O(n)
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {} 
    
        for i in nums:
            if i in freq:
                freq[i] += 1 
            else:
                freq[i] = 1 
        
        for i in freq:
            if freq[i] % 2 != 0:
                return False 
        
        return True 