# number = 234
# counter = 1
# # number %= 10
# number //= 10
# print(number)

number = int(input('Введите число: '))
counter_positive = 0
counter_negative = 0
while number != 0:
  if number > 0:
    counter_positive += 1
  else:
    counter_negative += 1
  number = int(input('Введите число: '))
print('Кол-во положительных чисел: ', counter_positive)
print('Кол-во отрицательных чисел: ', counter_negative)