import array as arr
array_num = arr.array('i', [1,1,2])

def removeDuplicates(array_num):
        # Length of the update array
        count = 0
        # Loop for all the elements in the array
        for i in range(len(array_num)):
            # If the current element is equal to the next element, we skip
            if i < len(array_num) - 2 and array_num[i] == array_num[i + 1]:
                continue
            # We will update the array in place
            array_num[count] = array_num[i]
            count += 1
        return count

print("length of array After removing duplicate elements from the sorted array:",removeDuplicates(array_num))