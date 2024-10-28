import numpy as np
matrix = []
str = list(map(int, input().split()))

while len(str) > 0:
    matrix.append(str)
    str = list(map(int, input().split()))
    
matrix = np.array(matrix)

check = (matrix == matrix.T)
print(np.all(check))