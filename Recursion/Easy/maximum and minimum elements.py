n = [1,2,4,6]

def max_min(n):
    global mx, mn
    mx = mn = n[0]
    def helper(n, x):
        global mx, mn
        if x == 0:
            return mx, mn
        else:
            if n[x-1] > mx:
                mx = n[x-1]
            elif n[x-1] < mn:
                mn = n[x-1]
            return helper(n , x-1)
    return helper(n, len(n))

mx, mn = max_min(n)
print("Max:", mx, "Min:", mn)

    
def find_max_min(input_array, min_value, max_value):
    if len(input_array) < 1:
        return min_value, max_value
    min_value = min(min_value, input_array[-1])
    max_value = max(max_value, input_array[-1])
    return find_max_min(input_array[:-1], min_value, max_value)

if __name__ == '__main__':
    input_array = [1, 3, 5, 7]
    
    min_value, max_value = find_max_min(input_array, input_array[0], input_array[0])
    print("Minimum value:", min_value)
    print("Maximum value:", max_value)
