minWidth = int(input('Enter minimal width: '))
maxWidth = int(input('Enter maximal width: '))

outSpace = int((maxWidth-minWidth)/2)
j = 0
i = 1

if minWidth > maxWidth:
    print("Maximal width mast be bigger then minimal width!!!")
else:
    if ((maxWidth - minWidth) % 2) != 0:
        print("The difference between maxWidth and minWidth must be a multiple of 2!!!")
    else:
        print(" "*outSpace, "*"*minWidth, sep="")
        while i < outSpace:
            print(" "*(outSpace-i), "*", " "*(minWidth+j), "*", sep="")
            i += 1
            j += 2

        while i > 0:
            print(" "*(outSpace-i), "*", " "*(minWidth+j), "*", sep="")
            i -= 1
            j -= 2

        print(" "*outSpace, "*"*minWidth, sep="")
