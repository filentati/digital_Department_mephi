import numpy as np
matrix = []
str = list(map(int, input().split()))

while len(str) > 0:
    matrix.append(str)
    str = list(map(int, input().split()))
    
matrix = np.array(matrix)

matrix_size = np.sum(matrix, axis = 0)

print(0 in matrix_size)
    