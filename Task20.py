'''Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.
Ввод:
ноутбук
Вывод:
12'''
import os,re
os.system('cls')
onePoint = 'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т' # строка
twoPoint = 'D, G, Д, К, Л, М, П, У' #строка
threePoint='B, C, M, P, Б, Г, Ё, Ь, Я' #строка
fourPoint = 'F, H, V, W, Y, Й, Ы' #строка
fivePoint = 'K, Ж, З, Х, Ц, Ч'#строка
eightPoint = 'J, X, Ш, Э, Ю'#строка
tenPoint = 'Q, Z, Ф, Щ, Ъ'#строка
keyList = [onePoint,twoPoint,threePoint,fourPoint,fivePoint,eightPoint,tenPoint] #список строк
print(keyList)
for element in keyList:
    element = element.split(", ")
print(keyList)
dictionaryPoint = {}
pointList = [1,2,3,4,5,8,10]
dictionaryPoint={}
for i in range(len(pointList)):
    key = keyList[i]
    dictionaryPoint[key]=pointList[i]
print(dictionaryPoint)
word = input("Enter the word ")
word = word.upper()
print(word)
cost = 0
for i in word:
    for key,value in dictionaryPoint.items():
        if i in key:
            cost = cost + value
print(cost)