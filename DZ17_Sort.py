"""
 Есть двумерный список из латинских букв, отсортировать буквы по колонкам.

Считаем, что список прямоугольный.

[['a', 'c', 'd']
 ['f', 'b', 'a']sep
 ['a', 'n', 'k']
 ['e', 'l', 'i']]
->
[['a', 'b', 'a']
 ['a', 'c', 'd']
 ['e', 'l', 'i']
 ['f', 'n', 'k']]
 """


m = [['a', 'c', 'd'], ['f', 'b', 'a'], ['a', 'n', 'k'], ['e', 'l', 'i']]
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
for r in rez:
    r.sort()
m = [[rez[j][i] for j in range(len(rez))] for i in range(len(rez[0]))]
print(*m, sep='\n')