print('Задача 8. Поменять местами: не всё так просто! (необязательная, повышенной сложности)')

# Вы уже умеете менять местами строковые переменные и знаете, 
# что в переменных кроме строк можно хранить и числа. 
# Напишите программу, которая меняла бы значения двух переменных местами, 
# но без использования третьей переменной и синтаксического сахара, который мы разбирали, а именно: 
# без конструкции a, b = b, a. В переменные будут вводиться только числа.

a = 7
b = 5
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)

# Реализуйте программу,
# которая получает на вход четырёхзначное число
# и выводит на экран каждую его цифру отдельно
# (в одну строчку либо каждая цифра в новой строчке).
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных

a = int(input('Введите четырехзначное число: '))
print(a // 1000, a // 100 % 10, a // 10 % 10, a % 10)

print(4587//10)