# Sum of 1 to N numbers
def Summation(firstNum, num):
    if firstNum > num:
        return 0
    return firstNum + Summation(firstNum+1, num)

num = int(input("Enter the number: "))

if num < 0:
    print("Enter a positive number")
else:
    print("Sum of 1 to N is : ", Summation(1, num))
