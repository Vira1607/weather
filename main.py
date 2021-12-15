print('Метеостанция')

# Программа принимает на вход три целых числа
# в градусах Цельсия: нижняя граница температуры, верхняя граница температуры и шаг.
#
# Программа выводит на экран
# таблицу соответствия градусов Цельсия градусам Фаренгейта
# от нижней до верхней границы с указанным шагом.

#
# Пример:
#
# Ввод:
# Нижняя граница: 0
# Верхняя граница: 50
# Шаг: 20
#
# Вывод:
# C        F

# 0        32
# 20       68
# 40       104
# 50       122

temperature_c = int(input('Нижняя граница: '))
border_top = int(input('Верхняя граница: '))
pace = int(input('Шаг: '))

print('C\t\tF')

while temperature_c < border_top:
  temperature_f = int(temperature_c * 1.8 + 32)
  print(str(temperature_c) + '\t\t' + str(temperature_f))
  temperature_c += pace

if temperature_c >= border_top:
  temperature_f = int(border_top * 1.8 + 32)
  print(str(border_top) + '\t\t' + str(temperature_f))
