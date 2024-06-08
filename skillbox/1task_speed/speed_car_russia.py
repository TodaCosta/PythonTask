print('Задание 1. Система расчёта штрафов')

car_speed = 147

is_town = True
is_camera = True

fine_for_20_to_40 = 500
fine_for_40_to_60 = 1000
fine_for_60_to_80 = 2000
fine_for_80_and_more = 5000

town_speed = 60
country_speed = 90

result_fine = 0

if is_town:
  over_speed = car_speed - town_speed
else:
  over_speed = car_speed - country_speed

if not is_camera and over_speed >= 60:
  print("Лишение водительских прав")

if over_speed < 0:
  result_fine = 0
  print("Скорость не превышена или превышена незначительно")
else:
  if over_speed >= 20 and over_speed < 40:
    result_fine = fine_for_20_to_40
  elif over_speed >= 40 and over_speed < 60:
    result_fine = fine_for_40_to_60
  elif over_speed >= 60 and over_speed < 80:
    result_fine = fine_for_60_to_80
  elif over_speed >= 80:
    result_fine = fine_for_80_and_more
  print("Штраф: " + str(result_fine))