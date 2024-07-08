# GCD or HCF

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

GCD = 0

#Brute force
for i in range(1, min(num1,num2)):
    if (num1 % i == 0) and (num2 % i == 0):
        GCD = max(i, GCD)

print("GCD of two numbers is : " + str(GCD))
