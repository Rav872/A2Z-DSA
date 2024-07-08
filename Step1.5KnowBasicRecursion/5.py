# Factorials of N numbers
def Factorial(num):
    if num == 1:
        return 1
    return num * Factorial(num-1)

num = int(input("Enter the number: "))

if num < 0:
    print("Enter the positive number")
else:
    print("Factorial of N is: ", Factorial(num))