#Задача 30

a1 = int(input('Введите первый элемент '))
d = int(input('Введите шаг '))
n = int(input('Введите количество элементов '))
for i in range(n):
   res = (a1 + i * d)
   print(res, end = ' ')

#Задача 32

list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input('Введите минимальный элемент '))
max_number = int(input('Введите максимальный элемент '))
for i in range(len(list)):
  if min_number <= list[i] <= max_number:
     print(i, end = ' ')