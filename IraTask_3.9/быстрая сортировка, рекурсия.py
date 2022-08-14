import random
# Быстрая сортировка
def rec(s):
    if len(s) <= 1:
        return s
    elem = s[0]  # can take element at any position
    left = list(filter(lambda x: x < elem, s))
    center = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem, s))
    return rec(left) + center + rec(right)
print(rec([3, 3, 1, 4, 10, 8]))  # [1, 3, 3, 4, 8, 10]

# Быстрая сортировка Хаора быстрее
def rec(s):
    if len(s) <= 1:
        return s
    elem = s[random.randint(0, len(s)-1)]
    left = list(filter(lambda x: x < elem, s))
    center = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem, s))
    return rec(left) + center + rec(right)
print(rec([3, 3, 1, 4, 10, 8]))  # [1, 3, 3, 4, 8, 10]

#Это всё медленнее, чем s.sort, потому что он написан на С++

x = ['a', 'dddd', 'сс', 'bbb']
x.sort(key=len)
print(x)

a = [5, 2, 3, 1, 4]
s = [5, 2, 3, 1, 4]
b = sorted(a)
list.sort(s)
print(b, a, s)