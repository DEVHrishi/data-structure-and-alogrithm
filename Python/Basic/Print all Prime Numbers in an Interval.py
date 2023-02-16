#tc= O(n^2)
n = list(map(int, input('Enter the numbers: ').split()))

prime=[]
for i in n:
    if i>1:
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            prime.append(i)
print(prime)

#tc=O(n*sqrt(n))
def print_prime_numbers(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** (1/2)) + 1):
                if (num % i) == 0:
                    break
            else:
                print(num)

start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))
print("Prime numbers in the given interval are:")
print_prime_numbers(start, end)



