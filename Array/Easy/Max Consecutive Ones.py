'''Given a binary array nums, return the maximum number of consecutive 1's in the array.
Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3'''

# TC = O(n) SC = O(n)
def findMaxConsecutiveOnes(self, nums) -> int:
        return len(max(''.join(map(str,nums)).split('0'),key=len))

# TC = O(n) SC = O(1)
def findMaxConsecutiveOnes(self, nums) -> int:
        res = 0
        count = 0
        for num in nums:
            if num == 0:
                count = 0
            else:
                count += 1
                res = max(res, count)
        
        return res

# TC = O(n) SC = O(n)
def findMaxConsecutiveOnes(self, nums) -> int:
        count = 0
        arr = []
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                arr.append(count)
                count = 0
        return max(arr)

