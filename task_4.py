# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях
import random

n = int(input('Введите число: '))
list = []

for i in range(n):
    num = random.randint(-n, n)
    list.append(num)
print(list)

a, b = map(int, input('Введите индексы двух элементов: ').split())
print(f'Произведение элементов равно: {list[a] * list[b]}')
