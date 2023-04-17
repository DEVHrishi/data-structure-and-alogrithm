'''Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]'''

from ast import List

# tc = O(n*logn) and sc = O(1)
def sortedSquares(self, A: List[int]) -> List[int]:
    for i in range(len(A)):
        A[i] *= A[i]
    A.sort()
    return A

# tc = O(n) and sc = O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # Two Pointer Approach
        n = len(nums)
        l, r = 0, n - 1
        k = n - 1
        ans = [0] * n
        while k >= 0:
            if abs(nums[l]) > nums[r]:
                ans[k] = nums[l] * nums[l]
                l += 1
            else:
                ans[k] = nums[r] * nums[r]
                r -= 1
            k -= 1
        return ans