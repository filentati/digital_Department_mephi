import numpy as np
import sys 

matrix = []

for string in sys.stdin:
    matrix.append(list(map(int, string.rstrip().split())))
    
matrix = np.array(matrix, float)

print((matrix.T - (matrix.mean(axis=1))).T)
