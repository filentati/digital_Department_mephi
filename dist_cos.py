import numpy as np
import sys 

matrix = []

for string in sys.stdin:
    matrix.append(list(map(int, string.rstrip().split())))
    
try:
    matrix = np.array(matrix)
    matrix = (matrix.T/np.linalg.norm(matrix, axis=1)).T
    cos_dist =[]
    for vector1 in range(matrix.shape[0]):
        for vector2 in range(vector1+1, matrix.shape[0]):
            cos_dist.append(np.dot(matrix[vector1], matrix[vector2]))
            
    cos_dist = np.array(cos_dist)
    cos_min = cos_dist.min()
    if np.isnan(cos_min):
        print('No solution')
    else:
        print(cos_min.round(2))
    
    
except ValueError:
    print('No solution')
    