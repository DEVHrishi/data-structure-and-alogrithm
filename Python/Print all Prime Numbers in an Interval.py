#tc= O(n)
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

#optimal code tc=O(n^0.5)
numbers = input('Enter the numbers: ').split()
numbers = [int(x) for x in numbers]

primes = []
for i in range(len(numbers)):
    if i > 1:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
print(primes)

