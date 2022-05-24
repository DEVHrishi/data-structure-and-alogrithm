import array as arr
array_num = arr.array('i', [1,1,1,2,3,3,4])
def removeDuplicates(array_num, var):
    count = 0
    for i in range(len(array_num)):
        if(array_num[i] != var):
            array_num[count] = array_num[i]
            count += 1
    return count

print("length of array After removing duplicate elements from the array:",removeDuplicates(array_num, 1))