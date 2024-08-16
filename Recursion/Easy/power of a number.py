def power_of_num(n, p):
    if p == 0:
        return 1
    else:
        return n * power_of_num(n, p-1)
print(power_of_num(2, 3))