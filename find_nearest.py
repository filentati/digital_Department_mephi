import numpy as np

mas = list(map(int, input().split()))

mas = np.array(mas)
mas_p = mas[mas>=0]
mas_m = mas[mas<0]
mas_mod=np.abs(mas_m)

if np.min(mas_p) < np.min(mas_mod):
    print(np.min(mas_p))
else:
    print(np.max(mas_m))