a = input().split()
d = {}
for i in a:
    d[i] = a.count(i)
print(len(d))

# лучше
print(len(set(input().split())))

