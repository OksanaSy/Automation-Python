"""
Напишите функцию to_dict(lst), которая принимает список из четного числа элементов и возвращает словарь, у которого
ключами будут элементы списка нечетные по порядку, а значениями - четные.

Считаем, что нечетные элементы списка оответствуют правилам задания ключей в словарях.



def to_dict(lst):
    pass

to_dict([1, 2, 3, 4])  # {1: 2, 3: 4}
"""


def to_dict(lst):
    result = map(lambda i: (lst[i], lst[i + 1]), range(len(lst) - 1)[::2])
    print(dict(result))


to_dict([1, 2, 3, 4])  # {1: 2, 3: 4}
