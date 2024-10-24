import numpy as np

matrix = []
k = int(input())
str = list(map(int, input().split()))

while len(str) > 0:
    matrix.append(str)
    str = list(map(int, input().split()))

matrix = np.array(matrix)

for i in range(matrix.shape[0]):
    if i%k == 0:
        for j in range(matrix.shape[1]):
            if j%k == 0:
                print(np.sum(matrix[(i):(k+i), (j):(k+j)]), end =' ')
        print('', end = '\n')