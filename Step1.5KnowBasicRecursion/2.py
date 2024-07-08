def printName(num):
    if num < 1:
        return 0
    print("Ravinder")
    num = num - 1
    printName(num)

num = int(input("Enter a number: "))
printName(num)