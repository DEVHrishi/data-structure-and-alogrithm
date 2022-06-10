'''Given an array nums of integers, return how many of them contain an even number of digits.'''

def findNumbers(nums):
        return sum((len(str(i))) % 2 == 0 for i in nums)

print(findNumbers([12,345,2,6,7896]))