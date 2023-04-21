"""Есть текстовый файл с данными пользователей.
Каждая строка определяет одного пользователя.В строке через точку с запятой указаны имя, возраст и список телефонов.
Если телефонов несколько, они разделены запятой.Прочитать файл и создать список из словарей с ключами 'name', 'age', 'phones'.
По каждому ключу записать соответствующее поле из файла.Поле имя обязательное. Если возраст или телефоны не указаны, точка с запятой все равно должны быть указаны в строке.
Имя записать в виде строки.Возраст записать в виде целого числа. Если возраст не указан или не возможно распарсить, записать None.
Телефоны записать списком строк. Если телефоны не указаны, записать пустой список.Если в имени или одном из телефонов есть ведущие или конечные пробелы, их надо удалить.
Полученный список:- записать в users_out.json файл
- записать в users_out.txt файл, по правилам исходного файла (возраст None или пустой список для телефонов должны преобразовываться в пустую строку)В исходном файле могут быть пустые строки.
Исходный файл может быть большим.Примеры файлов прикреплены.
Пример списка:[{'age': 34, 'name': 'user1', 'phones': ['+3804454545']},
{'age': 23, 'name': 'user2', 'phones': []},{'age': None, 'name': 'user3', 'phones': []},
{'age': None, 'name': 'user4', 'phones': ['+5635665335']},{'age': 25, 'name': 'user5', 'phones': ['+6563663', '+3333635635']},
{'age': None, 'name': 'user6', 'phones': []}]"""

import json

f = open("users.txt", "r")
raw = []
i = 1
for line in f:
    line = line.strip()
    if line != '':
        raw.append([item.strip() for item in line.split(';')])
f.close()
data = []
for stg in raw:
    # stg.pop()
    r1, r2, r3 = stg
    if r2.isdigit():
        r2 = int(r2)
    else:
        r2 = None
    if r3 != '':
        r3 = list(r3.replace(' ', '').split(','))
    else:
        r3 = []
    d = {'age': r2, 'name': r1, 'phones': r3}
    data.append(d)
json_object = json.dumps(data, indent=4)

with open("users_out.json", "w") as outfile:
    outfile.write(json_object)
outfile.close()
out = [*data]
with open('users_out.txt', 'w') as txtfile:
    for line in out:
        st = str(line['name']) + ';' + str(line['age']) + ';' + str(line['phones']) + '\n'
        txtfile.write(st.replace('None', '').replace('[', '').replace(']', '').replace('\'', ''))
txtfile.close()
