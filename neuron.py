n = int(input())
mas_w = list(map(int, input().split()))
b = int(input())
mas_x = list(map(int, input().split()))

def relu(x):
    if x > 0:
        return x
    else:
        return 0
    
if len(mas_w) == len(mas_x):
    sum = 0
    for i in range(n):
        sum += (mas_x[i])*mas_w[i]
    print(relu(sum + b))
    
else:
    print("No solution")
