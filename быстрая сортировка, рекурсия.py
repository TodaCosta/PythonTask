import random
import time
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



def QuickSort(A, l, r):
    if l >= r:
        return
    else:
        q = random.choice(A[l:r + 1])
        i = l
        j = r
        while i <= j:
            while A[i] < q:
                i += 1
            while A[j] > q:
                j -= 1
            if i <= j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
                QuickSort(A, l, j)
                QuickSort(A, i, r)

A=[4,5,7,1,8,99, 11]
r=len(A)-1
l=0
print(QuickSort(A, l, r)) #None
print(A) #[1, 4, 5, 7, 8, 11, 99]