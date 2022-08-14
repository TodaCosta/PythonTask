import itertools

n = [int(i) for i in input().split()]
s, l, m = [], [], []
for i in range(len(n)):
    if i % 2 == 0:
        l.append(n[i])
    elif i % 2 != 0:
        m.append(n[i])
for i, j in itertools.zip_longest(m, l, fillvalue=''):
    s += i, j
for i in s:
    if type(i) is int:
        print(int(i), end=' ')


# лучше:

digits = [int(c) for c in input().split()]
for i in range(1, len(digits), 2):
    digits[i - 1], digits[i] = digits[i], digits[i - 1]
print(*digits)
