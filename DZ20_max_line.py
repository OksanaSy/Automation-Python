"""
Есть текстовый файл. Вывести самую длинную строку.

Функции max, readlines не использовать. Файл может быть большим.


"""

f = open("text.txt", "r")
res = ""
maxLine = 0
for x in f:
    if maxLine < len(x):
        maxLine = len(x)
        res = x
print(res)
f.close()
