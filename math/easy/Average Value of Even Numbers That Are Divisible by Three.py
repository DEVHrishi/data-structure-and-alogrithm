'''Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.

Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

 

Example 1:

Input: nums = [1,3,6,10,12,15]
Output: 9
Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.
Example 2:

Input: nums = [1,2,4,7,10]
Output: 0
Explanation: There is no single number that satisfies the requirement, so return 0.'''

from typing import List

        
# tc = O(n) and sc = O(1)
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        c = 0
        s = 0
        for i in nums:
            if i%2==0 and i%3==0:
                s += i
                c += 1
        return s//c if c else c