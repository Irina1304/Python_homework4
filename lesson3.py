#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.
#Ввод: [1, 1, 2, 3, 4, 4, 4]
#Вывод: [2, 3]

from random import uniform

n = int(input('Введите размер списка: '))
list1 = []
for i in range(n):
    f = uniform(1, 4)
    list1.append(round(f))
print(list1)

found = set()
found_again = set()

for a in list1:
    if a in found_again:
        continue
    if a in found:
        found.remove(a)
        found_again.add(a)
    else:
        found.add(a)

print(list(found))




