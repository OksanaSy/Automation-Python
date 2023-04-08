numbers = [float(input("Enter first number: ")), float(input("Enter second number: ")), float(input("Enter third number: "))]
maxNum = numbers[0]
i = 0
while i < 3:
    if maxNum <= numbers[i]:
        maxNum = numbers[i]
    i += 1
print("Max number is: ", maxNum)
