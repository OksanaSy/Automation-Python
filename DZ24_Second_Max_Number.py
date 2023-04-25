"""
Написать функцию, на вход которой передают список чисел, а возвращает второе по величине число.

Если передали пустой список, функция должна вернуть None.

Из встроенных функций можно использовать только range и len.

Написать реализацию, которая выполняет только один проход списка.



def second_largest_number(lst):
    pass

second_largest_number([4, 2, 1, 5, 2, 5, 7])  # 5
second_largest_number([])  # None
"""


def second_largest_number(lst):
    if not lst:
        print('None')
    else:
        second_largest = lst[0]
        first_largest = lst[0]
        for i in range(len(lst)):
            if lst[i] > first_largest:
                second_largest = first_largest
                first_largest = lst[i]
            elif lst[i] > second_largest and lst[i] != first_largest:
                second_largest = lst[i]

        print(second_largest)


second_largest_number([4, 2, 1, 5, 2, 5, 7])  # 5
second_largest_number([])  # None
