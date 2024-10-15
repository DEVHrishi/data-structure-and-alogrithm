'''Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.

 

Example 1:

Input: nums = ["777","7","77","77"], target = "7777"
Output: 4
Explanation: Valid pairs are:
- (0, 1): "777" + "7"
- (1, 0): "7" + "777"
- (2, 3): "77" + "77"
- (3, 2): "77" + "77"
Example 2:

Input: nums = ["123","4","12","34"], target = "1234"
Output: 2
Explanation: Valid pairs are:
- (0, 1): "123" + "4"
- (2, 3): "12" + "34"
Example 3:

Input: nums = ["1","1","1"], target = "11"
Output: 6
Explanation: Valid pairs are:
- (0, 1): "1" + "1"
- (1, 0): "1" + "1"
- (0, 2): "1" + "1"
- (2, 0): "1" + "1"
- (1, 2): "1" + "1"
- (2, 1): "1" + "1"'''


from ast import List
from collections import Counter

# tc: o(n^2), sc: o(n)
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        c = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    c += 1
        return c
    
# tc: o(n*m), sc: o(n*m) where n is the length of nums and m is the avg length of nums
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        freq = Counter(nums)
        ans = 0 
        for k, v in freq.items(): 
            if target.startswith(k): 
                suffix = target[len(k):]
                ans += v * freq[suffix]
                if k == suffix: ans -= freq[suffix]
        return ans 
