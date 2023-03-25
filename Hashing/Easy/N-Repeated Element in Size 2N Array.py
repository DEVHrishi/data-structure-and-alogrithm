'''You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.

 

Example 1:

Input: nums = [1,2,3,3]
Output: 3
Example 2:

Input: nums = [2,1,2,5,3,2]
Output: 2
Example 3:

Input: nums = [5,1,5,2,5,3,5,4]
Output: 5'''

from ast import List


class Solution:
    from collections import Counter
    def repeatedNTimes(self, nums: List[int]) -> int:
        '''h = Counter(nums)'''
        h = {}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        z = max(h.values())
        for letter in h.keys():
            if h[letter] == z:
                return letter
                break

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        list1 = []
        for i in nums :
            if i in list1 :
                return i
            else :
                list1.append(i)

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hashmap={}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return nums[i]
            else:
                hashmap[nums[i]]=1
        

       