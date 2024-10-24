import numpy as np
import sys 

matrix = []

for string in sys.stdin:
    str = list(map(int, string.rstrip().split()))
    matrix.append(str)

matrix = np.array(matrix)

print(np.sum(np.all(matrix == 0, axis = 0)))