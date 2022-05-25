def add_data(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]

import array as arr
array_num = arr.array('i', [10, 11, 12, 13, 14, 16, 17, 18, 19, 20])
print('output pair:', add_data(array_num, 30))