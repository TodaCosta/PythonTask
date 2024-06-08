# def outer():   #внешняя функция
#     n = 5
#
#     def inner():  #вложенная функция
#         print(n)
#
#     inner()
#     print(n)
#
#
# outer()
#5
#5
from typing import List, Union, Any


# def outer():   #внешняя функция
#     n = 5
#
#     def inner():  #вложенная функция
#         nonlocal n
#         n = 25
#         print(n)
#
#     inner()
#     print(n)
#
#
# outer()

# a = str(input())
# print(a)
# b = str(input())
# print(a.find(b))

# print(input().find(input()))


# a, b = list(map(int, input().split(","))), int(input())
# if b not in a:
#     a.insert(b-1, b)
# print(a.index(b))



# n = int(input())
# m = [list(map(int, input().split())) for i in range(n)]
# b = []
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             b.append(m[i][j])
# print(sum(b))
#_______________________________________________
# nums = [int(i) for i in input().split(',')]
# f = []
# for i in nums:
#     if i == 0:
#         nums.pop(nums.index(i))
#         f.append(0)
# print(nums+f)

#то же
# nums = [int(i) for i in input().split(',')]
# print(sorted(nums, key=bool, reverse=True))


def add_binary(a, b):
    '''
    Возвращает сумму двух десятичных чисел в двоичном формате.
            Параметры:
                    a (int): первое десятичное целое число
                    b (int): второе десятичное целое число
            Возвращаемое значение:
                    binary_sum (str): двоичная строка суммы a и b
    '''
    binary_sum = bin(a+b)[2:]
    return binary_sum
print(add_binary.__doc__)

print(add_binary(4, 6))


numbers = [1, 5, 9, 6, 1, 2, 1]
print(numbers.count(1))


print([i for i in range(0,11)])

print([[x, y] for x in range(0, 2) for y in range(0, 3)])
numbers=[1,2,3,4]
print(numbers[::-1])

f=[5]
print(id(f))
g=[6]
f+=g
print(id(f))
print(f*2)
print(g)

# numbers = [1, 5, 9, 6, 1, 2, 1]
# print(numbers.index(5))

numbers = [1, 5, 9, 6]
print(numbers.pop(1))
print(numbers)

mylist = ['сайт', 'типичный', 'программист']
print(' '.join(mylist))


a=[1, 5, 2, 4]
b = [8,11,10,13]
print(a.sort())
print(b.sort())
print(a)
a=[1, 5, 2, 4]
b = [8,11,10,13]
print(sorted(a))
print(sorted(b))
print(a)


nums = [0,1,0,0,5]
print(sorted(nums, key=bool, reverse=True))
for i in nums:
    print(bool(i))

kk = [4, 5, 2, 1]
print(kk.pop(1))
kk = [4, 5, 2, 1]
del kk[1]
print(kk)
kk = [4, 5, 2, 1]
print(kk.remove(1))

ff = [5, 1, 77, 4]
gg = [5, 1, 77, 4]
ff.sort()
print(ff)
ll = sorted(gg)
print(gg)
print(ll)


v_1 = ['a', 1, 2, [0, 0]]
v_2 = v_1
print(v_2, v_1)
print(v_2 == v_1)
print(v_2 is v_1)
print(id(v_2), id(v_1))

s_1 = [1, 2, [0, 0]]
s_2 = s_1.copy()
print(s_2, s_1)
print(s_2 == s_1)
print(s_2 is s_1)
print(id(s_2), id(s_1))
s_1[2][0] = 77
s_2[2][0] = 66
print(s_2, s_1)

l_1 = [1, 2, [0, 0]]
l_2 = l_1[:]
print(l_2, l_1)
print(l_2 == l_1)
print(l_2 is l_1)
print(id(l_2), id(l_1))
l_1[2][0] = 99
l_2[0] = 101
print(l_2, l_1)


import copy

a6 = [1, [2, [3, 4], 5], 6]
b6 = copy.deepcopy(a6)
a6[0] = 111
a6[1][0] = 222
a6[1][1][0] = 333
print(b6)


kj = [1, 0, [99,100]]
lg = kj
kj[2][1] = 77
print(kj, lg)
lg[2][1] = 11
print(lg, kj)

vv = [2,5,7]
se = vv.copy()
vv[0]=1
se[1]=6
print(vv, se)
print(se)
print(vv)



dd1 = [2, 'h', [33, 0]]
dd_2 = dd1.copy()
dd1[0] = 'fool'
dd1[2][1] = 4
print(dd1)
print(dd_2)
dd_2[0] = 77
dd_2[2][1] = 77
print(dd1)
print(dd_2)
print(id(dd1[2]),id(dd_2[2]))
print(000000000000000000000000000000)

a6 = [1, [2, [3, 4], 5], 6]
b6 = copy.deepcopy(a6)
a6[0] = 111
a6[1][0] = 222
a6[1][1][0] = 333
print(b6)
print(a6)