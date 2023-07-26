'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X
5
1 2 3 4 5
6
-> 5'''
import os, random
os.system('cls')
number = int(input("Enter the Number "))
i=0
array = []
while i<number:
    array.append(i+1)
    i+=1
print(array)
searchNumber = int(input("Enter number for search "))
nearest = array[0]
for element in array:
    if abs(searchNumber-element)<abs(nearest-element):
        nearest=element
print(nearest)


