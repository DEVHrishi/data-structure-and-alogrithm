# tc = O(n^3)
X = [[1,2, 3], [4,5,6]]
Y = [[1,2, 3], [4,5,6]]

result = [[0,0,0], [0,0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)

# tc = O(n^2.37)

import numpy as np

def multiply_matrices_np(A, B):
    return np.matmul(A, B)

# Example usage
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])
C = multiply_matrices_np(A, B)

# Output:
# array([[ 58,  64],
#        [139, 154]])
