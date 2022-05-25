def count(arr_input):
    even = 0
    odd = 0
    for i in range(len(arr_input)):
        if arr_input[i] % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Number of even elements = ", even)
    print("Number of odd elements = ", odd)

count([2, 3, 4, 5, 6])