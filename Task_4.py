'''
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
многочлена и записать в файл (или вывести в терминал) многочлен степени k.

Пример:

- k = 2  => 2*x² + 4*x + 5
- k = 3  => 41*x^3 + 6*x² + 2*x + 98
'''

from random import randint

K = int(input('Введите степень k: '))

for i in range(K, 0, -1):          # range(старт, стоп, шаг)
    ratio = randint(1, 101)
    if ratio == 0: # randint начинается от 1
        continue
    elif ratio == 1:
        ratio = ''
    else:
        ratio = f'{ratio}·x^{i} +' if i != 1 else f'{ratio}·x +'
        print(ratio, end=' ')

print(f'{randint(1, 101)} = 0')
