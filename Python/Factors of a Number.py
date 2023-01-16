# TC=O(n)
def factors(n):
    fac = []
    for i in range(1, n+1):
        if(n%i == 0):
            fac.append(i)
    return fac

n = int(input('Enter a number: '))
print('factors of {}: {}'. format(n, factors(n)) )

# TC = (SQRT(n))
def factors(n):
    factors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            if i * i != n:
                factors.append(n // i)
        i += 1
    return factors

num = int(input("Enter a number: "))
print("The factors of", num, "are:",factors(num))
