def make_matrix(m):
    matrix = []
    i = 0
    while i != m:
        st = list(map(int, input().split()))
        matrix.append(st)
        i += 1
    return matrix

n, m = map(int, input().split())
sv = make_matrix(m)

w, h = map(int, input().split())
im = make_matrix(h)

size_w = w - n 
size_h = h - m 

val_stroka = 0
val_stolb = 0
while val_stroka <= size_w:
    while val_stolb <= size_h:
        val = 0
        for stolb in range(m):
            for stroka in range(n):
                val += sv[stroka][stolb]*im[stroka+val_stroka][stolb+val_stolb]
        print(val, end =" ")
        val_stolb += 1 
    print("", end = "\n")
    val_stolb = 0
    val_stroka += 1
        


