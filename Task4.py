# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти: '))

if quarter == 1:
    print('X > 0 and Y > 0')
elif quarter == 2:
    print('X < 0 < Y')
elif quarter == 3:
    print('X < 0 and Y < 0')
elif quarter == 4:
    print('X > 0 > Y')
else:
    print('Такой четверти нет')
