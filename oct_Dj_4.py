#Дано 32-битное целое число x, верните x развернув в обратную сторону. Если реверсирование x приводит к выходу
# значения за пределы 32-битного целочисленного диапазона со знаком [-231, 231-1], то верните 0.

# x =input()
# if int(x) >= 0:
#     x1 = x[::-1]
# else:
#     x1 = '-' + x[:0:-1]
# if -2147483648 <= int(x1) <= 2147483647:
#     print(int(x1))
# else:
#     print(0)



x = "121"
y = len(x)
center = y//2
print(center, x[y-1:center:-1])
if y % 2 == 0 and x[:center] == x[y-1:center-1:-1] or y % 2 != 0 and x[:center] == x[y-1:center:-1]:
    print("полидром")
else:
    print("нет")

#решение
x = "121"
print(x == x[::-1])


a = input()
def check(a):
    a = a.replace('[]', '').replace('()', '').replace('{}', '')
    return False if a else True
print(check(a))