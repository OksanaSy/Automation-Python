numbers = [input("Enter first number: "), input("Enter second number: "), input("Enter third number: ")]
i = 1
maxNum = numbers[0]

while i < 3:
    if maxNum <= numbers[i]:
        maxNum = numbers[i]
    i += 1
print("Max number is: ", maxNum)
