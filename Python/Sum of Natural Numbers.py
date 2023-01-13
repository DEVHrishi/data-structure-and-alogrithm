n = int(input('Enter a number: '))
m = int(input('Enter a number: '))

sum_of_natural_num = (n*(n+1))/2

print(int(sum_of_natural_num))

#2nd method
sum = 0

while m>0:
    sum+=m
    m-=1

print(int(sum))