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

counter = 0


def call_counter(file):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            f = open(file, "a")
            global counter
            counter += 1
            result = original_function(*args, **kwargs)
            st = f"Function 'add' was called {counter} times\n"
            f.write(st)
            f.close()
            return result

        return wrapper_function

    return decorator_function


@call_counter('data.txt')
def add(a, b):
    return a + b


print(add(4, 6))
print(add(4, 6))
