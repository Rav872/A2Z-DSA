# Give Nth fibonacci number (0 based indexing)
 
def fibonacci(firstNum, secondNum, index, num):
    if index == num:
        return secondNum
    return fibonacci(secondNum, firstNum+secondNum, index+1, num)
    
 
num = int(input("Enter the number: "))
if num <=0:
    print("Enter a positive number")
    exit
index = 1
firstNum = 0
secondNum = 1
 
print(num, "th fibonacci number is : ", fibonacci(firstNum, secondNum, index, num))