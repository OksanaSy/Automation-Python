n = int(input('Enter n: '))
i = 1
j = 1
space=1
for i in range(1, n+1):
    print(" "*(n*2 - space), *range(1, i), *range(i, 0, -1), sep=' ')
    i += 1
    space += 2


