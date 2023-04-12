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

word = input('Enter your frase: ')
x = word.lower().lstrip().rstrip()
if x == x[len(x)::-1]:
    print("True")
else:
    print("False")

"""
#2
word = input("Enter your frase: ").lower().strip()
val = True
for front in range(0, len(word)):
    for back in range(len(word), 0):
        if word[front] != word[back]:
            val = False
print(val)
"""

