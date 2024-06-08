""""
На вход программе подаётся натуральное число
n — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

Примечание. Элементы главной диагонали также учитываются.
"""

n = int(input())
m = [list(map(int, input().split()))[:n] for _ in range(n)]
k = 1
f = []
for i in m:
    f.append(max(i[:k]))
    k += 1
print(max(f))
#то же самое в 1 строку
print(max(e for i in range(int(input())) for e in map(int, input().split()[:i + 1])))


print([[i for i in range(1,4)] for e in range(4)]) #[[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
print([i for e in range(1,3) for i in range(4)]) #[0, 1, 2, 3, 0, 1, 2, 3]
print([[i for e in range(1,3)] for i in range(4)]) #[[0, 0], [1, 1], [2, 2], [3, 3]]



f = [(9, 12, 1), (5, 1, 3), (44, 8, 10)]
def hh(e):
    # for i in f:
    #     for j in i:
    #         print(j)
    return [j for i in f for j in i] #[9, 12, 1, 5, 1, 3, 44, 8, 10]

print(hh(f))
k = sorted(f, key=hh)
print(k)









