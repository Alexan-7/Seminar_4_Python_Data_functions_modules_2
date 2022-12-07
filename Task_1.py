'''
Вычислить число Pi c заданной точностью d, не используя ф. round()

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''

from math import pi
correct = int(input('Задайте точность числа Пи: '))
stroka = str(pi)
print(float(stroka[0:correct + 2]))  # срез от 0 до correct + '3' + '.'
