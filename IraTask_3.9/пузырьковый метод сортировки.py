
len_mas = 6 # длина списка
mas = [5, 7, 4, 3, 8, 2] # список
count_replacement = 0 #количество замен
for bubble in range(len_mas-1): # количество обходов
    for i in range(len_mas-1-bubble): # в этом цикле сравниваем соседние и меняем если 1 больше
        # он делает 1 обход от начала до конца списка
        # -bubble, что б не считал последние пузырьки
        if mas[i] > mas[i+1]:
            count_replacement += 1
            mas[i], mas[i+1] = mas[i+1], mas[i]

print(mas)
print(count_replacement)

