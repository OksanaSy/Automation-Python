"""
В программе есть строка multi_string. Строка состоит из предложений. Предложение - это набор символов, ограниченных точками или началом строки и точкой.

Записать в список количество слов в каждом предложении. Слово - набор символов между двумя пробелами или началом строки и пробелом.

Регулярные выражения не использовать.



multi_string = "Hello all. Here's pretty cold and hot. Choose yourself."
words_number -> [2, 5, 2]
"""

multi_string = """Hello all. Here's pretty cold and hot. Choose yourself."""
multi_string = multi_string.replace('.', '\n')
text = multi_string.split("\n")
token_list = []
for expr in text:
    token_list.append(len(expr.split()))
while token_list.count(0) != 0:
    token_list.remove(0)
print("words_number -> ", token_list)
