"""
Пользователь вводит адрес элемктронной почты. Вывести True, если строка является валидным адресом, иначе False.

Валидным адресом считаем, строку

- в которой встречается один раз '@' и один раз '.'

- '@' идет до '.'

- строка не начинается с '@' и не заканчивается '.'

В комментариях к коду должны быть указаны строки, которыми протестировали код

Регулярные выражения не использовать.


"""

email = input('Enter email: ')
if email.startswith("@") or email.endswith("."):
   print("False")
elif email.count('@') != 1 or email.count('.') != 1:
   print("False")
elif email.find('@') > email.find('.'):
   print("False")
else:
   print("True")

"""
sydoruk@gmail.com          True
sydoruk.ok@gmail.com       False
@oksana2@gmail.com         False
@oksana.com                False
oksana@gmail.              False
sydoruk@sumdu.edu.ua       False
SyDoRuK_@                  False
sydoruk.com                False
sydoruk@com                False
                           False
"""
