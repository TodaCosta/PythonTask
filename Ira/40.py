# for i in range(int(input())):
#     s = input()
#     virus = 'anton'
#     x = 0
#     for j in s:
#         if j == virus[x]:
#             x += 1
#         if x == 5:
#             print(i + 1, end=' ')
#             break
# n = 8
# matrix = [[0]*n for _ in range(n)]
# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()
#
# print_matrix(matrix, n)

# n = 5
# a = [[19, 21, 33, 78, 99],
#      [41, 53, 66, 98, 76],
#      [79, 80, 90, 60, 20],
#      [33, 11, 45, 67, 90],
#      [45, 67, 12, 98, 23]]
#
# maximum = -1
# minimum = 100
#
# for i in range(n):
#     if a[i][i] > maximum:
#         maximum = a[i][i]
#     if a[i][n - i - 1] < minimum:
#         minimum = a[i][n - i - 1]
# print(minimum + maximum)
#
# a = [int(input()) for j in range(int(i)) for i in  range(int(input()))]
# print(a)

n, m = int(input()), int(input())
matrix = []
tx = []
for i in range(n):
    matrix += [[input() for _ in range(m)]]
print(matrix)
# for line in matrix:
#     print(*line)
print()
b = [*map(list, zip(*matrix))]
for i in b:
    print(*i)


# a = [1, 2, "g"]
# b = ["g", 2, 9]
# f = [a, b]
# print(f)
# print(list(zip(*f)))
# print(map(list, zip(*f)))

n, m = int(input()), int(input())
matrix = []

for _ in range(n):
    row = [input() for j in range(m)]
    matrix.append(row)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

print()

for j in range(m):
    for i in range(n):
        print(matrix[i][j], end=' ')
    print()

