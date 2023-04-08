n = int(input('Enter n: '))
space=2
for i in range(1, n+1):
    st1=""
    st2=""
    for j in range(1, i):
        st1+=str(j)+" "
    for j in range(i,0,-1):
        st2+=str(j)+" "
    print(" "*(n*2 - space), st1, st2.rstrip(), sep='')
    space += 2

"""
n = int(input('Enter n: '))
i = 1
j = 1
space=1
for i in range(1, n+1):
    print(" "*(n*2 - space), *range(1, i), *range(i, 0, -1), sep=' ')
    i += 1
    space += 2

"""
