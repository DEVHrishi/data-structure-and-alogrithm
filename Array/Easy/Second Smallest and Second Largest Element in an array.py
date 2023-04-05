nums = [4, 2, 5, 5, 1, 9, 4]

min1 = min2 = float('inf')
max1 = max2 = float('-inf')
for n in nums:
    if n <= min1:
        min1, min2, = n, min1
    elif n < min2:
        min2 = n
    if n >= max1:
        max1, max2 = n, max1
    elif n > max2:
        max2 = n
print(max1, max2, min1, min2) 

