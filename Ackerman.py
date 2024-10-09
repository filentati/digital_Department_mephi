n, m = input().split()


# A(n, m) =A(n-1, A(n, m-1))

def A(n, m):
    if n == 0:
        return m + 1
    if m == 0:
        return A(n-1, 1)
    return A(n-1, A(n, m-1))

print(A(int(n), int(m)))
