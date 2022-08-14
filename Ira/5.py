a = [i for i in input().split()]
b = [a.pop(len(a)-1)]
b += a
print(*b)
# лучше
a = input().split()
print(*[a[-1]] + a[:-1])