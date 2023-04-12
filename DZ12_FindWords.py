"""
В программе есть строка s.

Вывести заголовком строку, котрая состоит из слов, в которых буква 'a' встречается два раза.



s = "aab qq c badcc a qqqqqaqqqqaa tpara"
Aab Tpara
"""
s = input("Enter text:")
words = s.split()
res = []
for word in words:
    if word.count('a') == 2:
        res.append(word.title())
print(*res)
