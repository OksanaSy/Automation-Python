"""
Есть список из не менее, чем двух float элементов.

Создать новый список, в котором между элементами исходного списка будут добавлены их средние значения.



lst = [3.5, 2, 4, 6.2, 8] ->
[3.5, 2.75, 2, 3.0, 4, 5.1, 6.2, 7.1, 8]
"""
lst = [3.5, 2, 4, 6.2, 8]
#size = int(input("Set size of list:"))
#if size <= 2:
if len(lst) <= 2:
    print("Size must be greater then 1")
else:
    #for i in range(size):
        #lst.append(float(input("Add float to list:")))
    print("lst=", lst)
    res = []
    #for i in range(size):
    for i in range(len(lst)):
        res.append(lst[i])
        #if i+1 < size:
        if i+1 < len(lst):
            res.append((lst[i]+lst[i+1])/2)
    print(res)
