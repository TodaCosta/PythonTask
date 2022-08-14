n = int(input())
a = []
for i in range(n):
    b = [1]*(i+1)
    for j in range(i+1):
        if j != 0 and j != i:
            b[j] = a[i-1][j-1] + a[i-1][j]
    a.append(b)
    print(b)
print(a)
