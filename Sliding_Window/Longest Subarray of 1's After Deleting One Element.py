'''Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.'''

# shrinkable
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        count = 0
        max_len = 0
        for j in range(len(nums)):
            count += (nums[j] == 0)
            while (count > 1):
                if nums[i] == 0:
                    count -= 1
                i += 1
            max_len = max(max_len , j-i)
        return max_len
    
# Non-shrinkable
class Solution:
    def longestSubarray(self, A: List[int]) -> int:
        i = 0
        cnt = 0  # State: count of zeros in the window
        N = len(A)
        
        for j in range(N):
            if A[j] == 0:
                cnt += 1  # Increment count of zeros when encountering zero
            
            # Shift the window when there are more than one zero
            if cnt > 1:
                if A[i] == 0:
                    cnt -= 1
                i += 1
        
        # Return the window size minus one because one element must be deleted
        return j - i