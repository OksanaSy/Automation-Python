"""
Найти сумму и произведение элементов списка больше числа MIN (включительно) и меньше числа MAX (включительно).

Если таких элементов нет, вывести ноль и для суммы, и для произведения.



lst = [2, 4, 6, 2, 1, 1, 9, 4, 6], MIN = 3, MAX = 6
sum_ = 20, product = 576
"""

lst1 = [2, 4, 6, 2, 1, 1, 9, 4, 6]
min1 = int(input("Enter MIN: "))
max1 = int(input("Enter MAX: "))
sum_ = 0
product = 1
itr = 0
for i in lst1:
    if max1 >= i >= min1:
        sum_ += i
        product *= i
    else:
        itr += 1
if itr == len(lst1):
    print("sum_ = 0, product = 0")
else:
    print("sum_ = ", sum_, ", product = ", product)
