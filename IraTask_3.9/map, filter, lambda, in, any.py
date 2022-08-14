# a = list(map(int, input().split()))
# print(a)
a = [1, "карт", 99, 4, 5, 6, 7, 8, 9]
b = ["карточка", 5, 7]
def binar(list, item):
    if item in list:
        print("Yes", list.index(item)) # Yes 2
        print(any(word in a for word in b)) # True


binar(a, 99)
# ________________________________________________


def z(x):
    return x % 2 == 0


y = [1, 2, 99, 4, 5, 6, 7, 8, 9]
print(list(map(z, y))) # [False, True, False, True, False, True, False, True, False]
print(list(filter(z, y))) # [2, 4, 6, 8]
print(list(map(lambda i: i*2, y))) # [2, 4, 198, 8, 10, 12, 14, 16, 18]
# __________________________________

def Sort(data):
    for i in range(0, len(data)):
        minIndex = i
        for j in range(i + 1, len(data)):
            if data[j] < data[minIndex]:
                minIndex = j
                if minIndex != i:
                    data[i], data[minIndex] = data[minIndex], data[j]
    print(data)
Sort(y)