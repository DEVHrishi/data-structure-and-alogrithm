def findNumbers(nums):
        return sum((len(str(i))) % 2 == 0 for i in nums)

print(findNumbers([12,345,2,6,7896]))