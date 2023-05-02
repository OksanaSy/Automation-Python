"""
Написать декоратор с параметром. Если применить его к функции, он будет выводить в файл, который передали параметром, сколько раз вызывалась функция на момент вызова.



@call_counter('data.txt')
def add(a, b):
    return a + b

print(add(4, 6))
print(add(4, 6))
data.txt content:

Function 'add' was called 1 times
Function 'add' was called 2 times
"""

"""Написать декоратор с параметром.
Если применить его к функции, он будет выводить в файл, который передали параметром,
 сколько раз вызывалась функция на момент вызова.
"""
"""Написать декоратор с параметром.
Если применить его к функции, он будет выводить в файл, который передали параметром,
 сколько раз вызывалась функция на момент вызова.
"""
counter = {}


def call_counter(file):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            with open(file, 'a') as f:
                global counter
                result = original_function(*args, **kwargs)
                if (original_function.__name__ not in counter):
                    counter[original_function.__name__] = 1
                else:
                    counter[original_function.__name__] += 1
                st = f"Function {original_function.__name__} was called {counter[original_function.__name__]} times\n"
                f.write(st)
            return result

        return wrapper_function

    return decorator_function


@call_counter('data4.txt')
def add(a, b):
    return a + b


@call_counter('data4.txt')
def mult(a, b):
    return a * b


print(add(4, 6))
print(mult(4, 6))
print(add(4, 6))
print(mult(4, 6))
print(add(4, 6))
print(mult(4, 6))
