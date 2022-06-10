'''Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].'''

# brute force method tc = O(n) sc = O(1)
def shuffle(nums, n):
    arr = []
    for i in range(n):
        arr += [nums[i]]
        arr += [nums[i+n]]
    return arr

print(shuffle())

# divide and conquer tc = O(n) sc = O(1)

def shuffle(nums, n):
    l = len(nums)
    left = nums[:(l//2)]
    r = nums[l//2::]
    res = []
    for i in range(l//2):
        res.append(left[i])
        res.append(r[i])
    return res
