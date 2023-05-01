"""
Написать генераторную функцию, которая принимает два параметра m, n.

Генератор должен возвращать числа от 1 до n (включительно), затем числа от 1 до n в квадрате, и так до степени m (включительно)



for i in generator(3, 4):
    print(i)
# 1, 2, 3, 4, 1, 4, 9, 16, 1, 8, 27, 64
"""


def generator(m, n):
    p, num, res = 1, 1, []
    for p in range(1, m+1):
        for num in range(1, n+1):
            res.append(pow(num, p))
    return res


for i in generator(3, 4):
    print(i, end=" ")