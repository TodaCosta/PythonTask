h = [6, 6, 7, 7]


def fff(*h):
    for i in h:
        return i


# a = list(int(i) for i in input().split(','))
# b = int(input())
print(fff(h))
print(*fff(h))
"""
Звездочка перед аргументом в заголовке функции "собирает" 
все позиционные (перечисленные последовательно) аргументы в кортеж.
добавьте * перед аргументом при вызове функции(чтобы список "распаковался" в отдельные аргументы)
"""

ki = [3, 4, 6, 1, 5, -1]
fi = 5
g = []
for i in range(len(ki)):
    if i + 1 < len(ki):
        for j in range(i + 1, len(ki)):
            if ki[i] + ki[j] == fi:
                g.append(ki[i])
                g.append(ki[j])
                print(g)

s = [-7, 5, 6, -2, 11]
l = 4
s1 = []
for i in range(len(s)):
    if i + 1 < len(s):
        for j in range(i + 1, len(s)):
            if s[i] + s[j] == l:
                s1.append(s[i])
                s1.append(s[j])
    break
print(s1)
"""
_________________________________________________

"""



def first_sum_index():
    for i in range(len(a)):
        if i < len(a):
            for j in range(i+1, len(a)):
                if a[i] + a[j] == b:
                    d.append(a[i])
                    d.append(a[j])
        if len(d) > 1:
            break
    return d


a = [int(r) for r in input().split(',')]
b = int(input())
d = []
print(first_sum_index())

a = [int(r) for r in input().split(',')]
b = int(input())
d = []
for i in range(len(a)):
    if i < len(a):
        for j in range(i+1, len(a)):
            if a[i] + a[j] == b:
                d.append(i)
                d.append(j)
    if len(d) != 0:
        break
print(d)


x = list(map(int, input().split(',')))
y = int(input())
print([[i, j] for i in range(len(x)) for j in range(i+1, len(x)) if x[i]+x[j] == y][0])


h1 = list(map(int, input().split(',')))
h2 = int(input())
print([[i, j] for i in range(len(h1)) for j in range(i+1, len(h1)) if h1[i] + h1[j] == h2][0])

