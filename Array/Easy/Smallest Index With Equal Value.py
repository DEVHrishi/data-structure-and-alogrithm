def smallestEqual(nums):
        for idx, val in enumerate(nums):
            if idx % 10 == val:
                return idx
        return -1

print(smallestEqual([1,2,3,4,5,6,7,8,9,0]))