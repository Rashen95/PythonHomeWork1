# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

import random
x = random.choice([True, False])
y = random.choice([True, False])
z = random.choice([True, False])

print(x)
print(y)
print(z)

if not(x or y or z) == (not x and not y and not z):
    print('Истина')
else:
    print('Ложь')
