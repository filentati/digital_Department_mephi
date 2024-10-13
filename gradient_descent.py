from math import sin
x0, N, L = input().split()
x0 = float(x0)
N = int(N)
L = float(L)

n = 0
while n < N:
    x_new = x0 - L*(2*x0-15*sin(x0))
    x0 = x_new
    n += 1

if x_new != int(x_new):
    print(round(x_new, 4))
    #print(f"{x_new:.4f}")
else:
    print(float(x_new))
    