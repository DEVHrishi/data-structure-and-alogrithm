list = [1,3,5,6,9]

for index, value in enumerate(list):
    print(index, value)

for index, value in enumerate(list, start=1):
    print(index, value)

for index in range(len(list)):
    value = list[index]
    print(index, value)