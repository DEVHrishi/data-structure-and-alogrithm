# Python3 code to implement factorial

# Factorial function
def f(n):

    # Stop condition
    if (n == 0 or n == 1):
        return 1

    # Recursive condition
    else:
        return n * f(n - 1)

# Driver code
if __name__ == '__main__':

    n = 5
    print("factorial of", n, "is:", f(n))


# A tail recursive function
def Recur_facto(n, a=1):

    if (n == 0):
        return a

    return Recur_facto(n - 1, n * a)


# print the result
print(Recur_facto(6))
