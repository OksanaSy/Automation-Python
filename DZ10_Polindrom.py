"""
Пользователь вводит строку. Вывести True, если строка является палиндромом, иначе False.

Палиндром - строка, которя читается одинаково слева и справа.

Если в строке есть ведущие или конечные пробелы, они не учитываются.

Проверка должна быть регистронезависимой.

Решить минимум двумя способами.



"    aBC cba " # True
"a BCQcb a    " # True
" ab bca"  # False
"""

#1
"""
word = input('Enter your frase: ')
x = word.lower().strip()
if x == x[::-1]:
    print("True")
else:
    print("False")

"""
#2
str1 = input('Enter your frase: ').strip().lower()
result = True
for i in range(0, int(len(str1)/2)):
    if str1[i] != str1[len(str1)-i-1]:
        result = False
        break
print(result)
