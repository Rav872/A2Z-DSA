def printFunc(num):
    if (num < 1):
        return 0
    print("Hello")
    num = num - 1
    printFunc(num)

printFunc(10)
