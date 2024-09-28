'''You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.
Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].'''


from ast import List
import heapq

# tc: O((len(nums) - k) * n), sc: O(1)
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        while len(nums) > k:
            nums.remove(min(nums))
        return nums
    
# tc: O(nlogn), sc: O(n)
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = [(nums[i], i) for i in range(len(nums))]
        arr.sort(reverse=True)

        arr = arr[:k]
        arr.sort(key=lambda k: k[1])

        return [val[0] for val in arr]
    
# tc: O(n + k log n) and sc: O(n)
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = [(-nums[i], i) for i in range(len(nums))]
        heapq.heapify(arr)

        ans = []
        while k > 0:
            ans.append(heapq.heappop(arr))
            k -= 1

        ans.sort(key=lambda k: k[1])
        return [-val[0] for val in ans]