"""
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
4
1 0 0 1
7 7 8 2
3 0 0 3
#8


n = int(input())
m = [list(map(int, input().split()))[:n] for _ in range(n)]
g = []
for i in range(len(m)):
    for j in range(len(m[i])):
        if i >= j and i <= n-1-j:
            g.append(m[i][j])
        if i <= j and i >= n-1-j:
            g.append(m[i][j])
print(max(g))
"""

n = int(input())
m = [list(map(int, input().split()))[:n] for _ in range(n)]
top = []
right = []
left = []
bottom = []
for i in range(len(m)):
    for j in range(len(m[i])):
        if i != j and i != n-1-j:
            if i > 0 and i < n-1 and j > n/ 2:
                right.append(m[i][j])
            if i > 0 and i < n-1 and j < n/2:
                left.append(m[i][j])
            if i == 0:
                top.append(m[i][j])
            if i == n-1:
                bottom.append(m[i][j])
print("Верхняя четверть: ", sum(top))
print("Правая четверть: ", sum(right))
print("Нижняя четверть: ", sum(bottom))
print("Левая четверть: ", sum(left))


s=[[1, 2, 3]]
print(s*3)


d = ['ва','рот','аква']
d.sort()
print(d)

