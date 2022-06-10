'''Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if such index does not exist.

x mod y denotes the remainder when x is divided by y.'''

def smallestEqual(nums):
        for idx, val in enumerate(nums):
            if idx % 10 == val:
                return idx
        return -1

print(smallestEqual([1,2,3,4,5,6,7,8,9,0]))