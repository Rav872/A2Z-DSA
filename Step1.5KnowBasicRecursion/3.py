# Sum of N to 1 numbers
def Summation(num):
    if num == 0:
        return 0
    return num + Summation(num-1)

num = int(input("Enter the number:  "))
print("Sum is : ", Summation(num))