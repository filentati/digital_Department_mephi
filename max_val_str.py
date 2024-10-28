import numpy as np
matrix = []
str = list(map(int, input().split()))

while len(str) > 0:
    matrix.append(str)
    str = list(map(int, input().split()))
    
matrix = np.array(matrix)

sum_string = np.sum(matrix, axis = 1)
max_sum = np.max(sum_string)
print(*np.where(sum_string == max_sum)[0])