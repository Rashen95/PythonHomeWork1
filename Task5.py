# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

distance = 0
x1 = int(input('Координата Х первой точки: '))
y1 = int(input('Координата Y первой точки: '))
x2 = int(input('Координата Х второй точки: '))
y2 = int(input('Координата Y второй точки: '))

print(round(math.sqrt((x2-x1)**2+(y2-y1)**2), 2))
