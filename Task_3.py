'''
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
элементов исходной последовательности.(Вывод тех элементов, которые были без повторов)

Ввод: 1 2 3 2 4 4
Вывод: 1 3
'''

from random import randrange

quantity = 10
list1 = [randrange(5) for i in range(quantity)]
print('Список из случайных чисел:', *list1)

list2 = []
for k in list1:
    b = 0
    for g in list1:
        if k == g:
            b += 1
    if b == 1:
        list2.append(k)
print('Уникальные элементы списка:', *list2)

#     if list1.count(k) == 1:
#         list2.append(k)
# print('Уникальные элементы списка', *list2)