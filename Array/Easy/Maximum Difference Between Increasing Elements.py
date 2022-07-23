'''Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.

Example 1:

Input: nums = [7,1,5,4]
Output: 4
Explanation:
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.'''

def maximumDifference(self, nums) -> int:
        curr_min = nums[0]
        ans = 0
        
        for i in nums:
            if i < curr_min:
                curr_min = i
                
            ans = max(ans, i-curr_min)
            
        return -1 if ans == 0 else ans 