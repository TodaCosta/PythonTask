n = int(input())
a = []
for i in range(n+1):
    b = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            b[j] = a[i - 1][j - 1] + a[i - 1][j]
    a.append(b)
for i in a:
    print(i)
