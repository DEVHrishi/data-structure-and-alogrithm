def function(x):
    array = []

    for num in x:
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            
            array.append(num)

    return len(array)


z = [4, 5, 6, 7, 8, 9, 10]
print(function(z))