"""
Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке,
больших среднего арифметического элементов данной строки.
"""

n = int(input())
# m = [[int(i) for i in input().split()] for j in range(n)]
m = [list(map(int, input().split())) for _ in range(n)]
for i in m:
    k = sum(i) / n
    l = []
    for j in i:
        if j > k:
            l.append(j)
    print(len(l))
