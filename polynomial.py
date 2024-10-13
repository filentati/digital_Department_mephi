val= list(map(int, input().split()))
a = val[0]
b = val[1]
c = val[2] - val[3]

if a == 0 and b  == 0:
    if c == 0:
        dec = -1
    else: 
        dec = 0
elif a == 0:
    dec = 1
elif (b**2 - 4*a*c) < 0:
    dec = 0
elif (b**2 - 4*a*c) == 0:
    dec = 1
else:
    dec = 2

print(dec)