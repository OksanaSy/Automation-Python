"""
Написать функцию, которая принимает несколько последовательностей,
и возвращает список из кортежей составленных из элементов последовательностей одного индекса.
Функция также должна принимать параметры с дефолтными значения:
full=False - по умолчанию "склеить" послдовательности по кратчайшей, иначе по самой длинной
default=None - если full=True, вместо недостающих элементов поставить значение указанное в параметре default
Встроенную функцию zip не использовать.
"""
import copy


def custom_zip(*sequences, full=False, default=None):
    res = []
    stunt_double = copy.deepcopy(sequences)
    if not full:
        size = min(len(item) for item in stunt_double)
        for i in range(size):
            tmp = tuple(iter[i] for iter in stunt_double)
            res.append(tmp)
    else:
        size = max(len(item) for item in stunt_double)
        for i in range(size):
            for element in stunt_double:
                try:
                    check = element[i]
                except IndexError:
                    element.append(default)
            tmp = tuple(element[i] for element in stunt_double)
            res.append(tmp)
    return res


seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
assert custom_zip(seq1, seq2) == [(1, 9), (2, 8), (3, 7)]
assert custom_zip(seq1, seq2, full=True, default="Q") == [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]
