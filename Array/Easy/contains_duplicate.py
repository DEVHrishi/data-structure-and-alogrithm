# brute force tc = O(n^2) sc = O(1)
def duplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# use sort method tc = O(nlogn) sc = O(1)
def duplicate(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

# use set() method tc = O(n) sc = O(n)
def duplicate(nums):
    return len(set(nums)) != len(nums)

# use hash table method tc = O(n) sc = O(n)
def duplicate(nums):
    d = {}
    for i in range(len(nums)):
        if nums[i] in d:
            return True
        else:
            d[nums[i]] = 1
    return False