'''You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.

 

Example 1:

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
2- Reverse subarray [4,2], arr becomes [1,2,4,3]
3- Reverse subarray [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
Example 2:

Input: target = [7], arr = [7]
Output: true
Explanation: arr is equal to target without any reverses.
Example 3:

Input: target = [3,7,9], arr = [3,7,11]
Output: false
Explanation: arr does not have value 9 and it can never be converted to target.'''

from ast import List

# tc = O(nlogn) and sc = O(n)
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        l = sorted(arr)
        m = sorted(target)
        return l == m

# tc = O(n) and sc = O(n)
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # return counter(target) == counter(arr). it also works
        l = {}
        m = {}
        for i in arr:
            if i in l:
                l[i] += 1
            else:
                l[i] = 1
        for i in target:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        return l == m