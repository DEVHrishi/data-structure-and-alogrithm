'''Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]'''

from ast import List

# tc = O(n) and sc = O(1)
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n==1:
            return nums
        i,j=0,1
        while j<n:
            if nums[i]%2!=0:
                if nums[j]%2==0:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
            else:
                i+=1
            j+=1
        return nums
    
# tc = O(n) and sc = O(n)
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        e = []
        o = []
        for i in nums:
            if i % 2 == 0:
                e.append(i)
            else:
                o.append(i)
        return e+o