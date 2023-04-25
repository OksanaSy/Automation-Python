"""
Напишите функцию read_last(file_path, symbol_number), которая выводить на печать построчно последние symbol_number символов в каждой строке (перевод строки не учитывать).

Пустые строки - пропускать.



def read_last(file_path, symbol_number):
    pass

read_last('read_last.txt', 6)


read_last.txt ->
456789
345678
234567
Line5
"""


def read_last(file_path, symbol_number):
    f = open(file_path, "r")
    for line in f:
        line = line.replace('\n', '')
        if line != '':
            print(line[-symbol_number:])
    f.close()


read_last('read_last.txt', 6)
