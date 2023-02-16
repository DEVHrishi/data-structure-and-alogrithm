x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[j][i] 

for r in result:
    print(r)


''' Program to transpose a matrix using list comprehension'''

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

for r in result:
   print(r)