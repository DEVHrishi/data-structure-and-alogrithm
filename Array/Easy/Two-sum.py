# brute force method tc=O(n^2) sc=O(1)
def twoSum(num, target):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] + num[j] == target:
                return [i, j]


print('output:', twoSum([2, 7, 11, 15], 9))

#efficient approach tc=O(n) sc=O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


input_list = [2, 8, 12, 15]
ob1 = Solution()
print(ob1.twoSum(input_list, 20))
