print('Задание 2. Система штрафов в Германии')

car_speed = 111
is_town = True
"""
1-ый индекс в списке - штраф в населенных пунктах,
2-ой индекс в списке - штраф вне населенных пунктов
"""
fine_for_1_to_10 = [30, 20]
fine_for_11_to_15 = [50, 40]
fine_for_16_to_20 = [70, 60]
fine_for_21_to_25 = [115, 100]
fine_for_26_to_30 = [180, 150]
fine_for_31_to_40 = [260, 200]
fine_for_41_to_50 = [400, 320]
fine_for_51_to_60 = [560, 480]
fine_for_61_to_70 = [700, 600]
fine_for_70_and_more = [800, 700]
"""
Данные о разрешённой скорости в населенных пунктах и вне населенных пунктов в Германии
взяты из открытых источников в интернете.
"""
town_speed = 50
country_speed = 100

result_fine = 0

# over_speed = car_speed - town_speed if is_town else car_speed - country_speed
if is_town:
    over_speed = car_speed - town_speed
else:
    over_speed = car_speed - country_speed

if over_speed < 0:
    result_fine = 0
    print("Скорость не превышена или превышена незначительно")
else:
    if is_town:
        if over_speed <= 1 and over_speed < 10:
            result_fine = fine_for_1_to_10[0]
        elif over_speed <= 11 and over_speed < 15:
            result_fine = fine_for_11_to_15[0]
        elif over_speed <= 16 and over_speed < 20:
            result_fine = fine_for_16_to_20[0]
        elif over_speed <= 21 and over_speed < 25:
            result_fine = fine_for_21_to_25[0]
        elif over_speed <= 26 and over_speed < 30:
            result_fine = fine_for_26_to_30[0]
        elif over_speed <= 31 and over_speed < 40:
            result_fine = fine_for_31_to_40[0]
        elif over_speed >= 41 and over_speed < 50:
            result_fine = fine_for_41_to_50[0]
        elif over_speed >= 51 and over_speed < 60:
            result_fine = fine_for_51_to_60[0]
        elif over_speed >= 61 and over_speed < 70:
            result_fine = fine_for_61_to_70[0]
        elif over_speed >= 70:
            result_fine = fine_for_70_and_more[0]
    else:
        if over_speed <= 1 and over_speed < 10:
            result_fine = fine_for_1_to_10[1]
        elif over_speed <= 11 and over_speed < 15:
            result_fine = fine_for_11_to_15[1]
        elif over_speed <= 16 and over_speed < 20:
            result_fine = fine_for_16_to_20[1]
        elif over_speed <= 21 and over_speed < 25:
            result_fine = fine_for_21_to_25[1]
        elif over_speed <= 26 and over_speed < 30:
            result_fine = fine_for_26_to_30[1]
        elif over_speed <= 31 and over_speed < 40:
            result_fine = fine_for_31_to_40[1]
        elif over_speed >= 41 and over_speed < 50:
            result_fine = fine_for_41_to_50[1]
        elif over_speed >= 51 and over_speed < 60:
            result_fine = fine_for_51_to_60[1]
        elif over_speed >= 61 and over_speed < 70:
            result_fine = fine_for_61_to_70[1]
        elif over_speed >= 70:
            result_fine = fine_for_70_and_more[1]
    print("Штраф: " + str(result_fine))
