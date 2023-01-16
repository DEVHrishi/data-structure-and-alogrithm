def compute_GCD(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if ((x%i == 0) and (y%i == 0)):
            hcf = i
    return hcf

print(compute_GCD(54, 24))

def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

print(GCD(54, 24))














