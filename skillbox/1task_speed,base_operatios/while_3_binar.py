hidden_number = int(input('Загадайте число от 1 до 100: '))
left = 1
right = 100
number = False
answer = 0

while answer != 1 and not number:
    middle = (left + right) // 2
    print('Твое число равно, меньше или больше, чем число ' + str(middle) + '?')
    answer = int(input('1 — равно, 2 — больше, 3 — меньше: '))
    if answer == 1:
        number = True
        print(middle)
    elif answer == 3:
        right = middle - 1
    elif answer == 2:
        left = middle + 1















# number = 50
# left = number
#
# print('Твое число равно, меньше или больше, чем число ' + str(number) + '?')
# answer = int(input('1 — равно, 2 — больше, 3 — меньше: '))
#
#
#
# while number != hiden_number:
#     if answer == 2:
#         if number > 50:
#             left = number
#             number = (100 - number) // 2 + left
#             print('Твое число равно, меньше или больше, чем число ' + str(number) + '?')
#             answer = int(input('1 — равно, 2 — больше, 3 — меньше: '))
#         else:
#             left = number
#             if number == 1:
#                 left = 2
#             number = number // 2 + left
#             print('Твое число равно, меньше или больше, чем число ' + str(number) + '?')
#             answer = int(input('1 — равно, 2 — больше, 3 — меньше: '))
#     elif answer == 1:
#         break
#     else:
#         if number > 50:
#             left = number
#             print(number)
#             number = (100 - number) // 2 + left
#             print('Твое число равно, меньше или больше, чем число ' + str(number) + '?')
#             answer = int(input('1 — равно, 2 — больше, 3 — меньше: '))
#         else:
#             number = number // 2
#             print('Твое число равно, меньше или больше, чем число ' + str(number) + '?')
#             answer = int(input('1 — равно, 2 — больше, 3 — меньше: '))
