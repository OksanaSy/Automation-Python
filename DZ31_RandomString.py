"""Написать функцию, которая возвращает слуайную строку заданной длины.
Строка должна состоять из больших и маленьких латинских букв и цифр.
(снижать за это оценку не буду, но лучше постараться сделать так, чтобы символы попадали в строку равномерно)
"""
import random


def get_random_string(length: int) -> str:
    res = ''
    for i in range(length):
        # 48-57 digits,65-90 upper case,97-122 lower case
        num = random.choices([random.randint(48, 57), random.randint(65, 90), random.randint(97, 122)],
                             weights=[1, 1, 1])
        res += ''.join(chr(num[0]))
    return res


print(get_random_string(10))
"""
Ограничения:
- Не использовать модуль string
- Не создавать руками список ['a', 'b', 'c', ..., 'X', 'Y', 'Z', 0, 1, ..., 8, 9]
"""
