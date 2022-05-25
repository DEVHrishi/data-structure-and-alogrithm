import array as arr
array_num = arr.array('i', [10, 11, 12, 13, 14, 16, 17, 18, 19, 20])
min = array_num[0]
max = array_num[0]
for i in range(len(array_num)):
    if array_num[i] < min:
        min = array_num[i]
    if array_num[i] > max:
        max = array_num[i]

print('min:', min)
print('max:', max)