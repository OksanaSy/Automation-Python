"""
Выборка из списка словарей

Есть список состоящий из словарей. Каждый словарь описывает пользователся и имеет два ключа: 'name' (str) и 'age' (int).

Создать и вывести список имен пользователей чей возраст от 18 лет (включительно).



users = [
{'name': 'Luarvik L. Luarvik',
'age': 17},
{'name': 'Olaf Andvarafors',
'age': 18},
{'name': 'Brun Du Barnstokr',
'age': 19}
]


['Olaf Andvarafors', 'Brun Du Barnstokr']

"""
users = [
{'name': 'Luarvik L. Luarvik',
'age': 17},
{'name': 'Olaf Andvarafors',
'age': 18},
{'name': 'Brun Du Barnstokr',
'age': 19}
]

res = []
for usr in users:
    if usr['age'] >= 18:
        res.append(usr['name'])
print(res)
