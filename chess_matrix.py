import numpy as np

n = int(input())

matrix = np.zeros((n, n), dtype=int)
matrix[1::2, ::2] = 1
matrix[::2, 1::2] = 1
for i in matrix:
    print(*i)