'''Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 

Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12'''

# approach 1: find 2 max numbers in 2 loops. T = O(n). S = O(1)
# approach 2: sort and then get the last 2 max elements. T = O(n lg n). S = O(1)
# approach 3: build min heap of size 2. T = O(n lg n). S = O(1)
# python gives only min heap feature. heaq.heappush(list, item). heapq.heappop(list)
from ast import List
import heapq


class Solution:
    # tc: O(n), sc: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        max_1 = max(nums)
        nums.remove(max_1)
        max_2 = max(nums)
        return (max_1-1)*(max_2-1)
    
    # tc: O(n lg n), sc: O(1)
    def maxProduct2(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)
    
    # tc: O(n lg n), sc: O(1)
    def maxProduct3(self, nums: List[int]) -> int:
        heap = [-1]
        for num in nums:
            if num > heap[0]:
                if len(heap) == 2:
                    heapq.heappop(heap)
                heapq.heappush(heap, num)
                
        return (heap[0]-1) * (heap[1]-1)
    
    # tc: O(n lg n), sc: O(n)
    def maxProduct(self, nums: List[int]) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)
        return ((-heapq.heappop(heap))-1) * ((-heapq.heappop(heap))-1)
