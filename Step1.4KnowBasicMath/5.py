# Armstrong number

import math

num1 = int(input("Enter the number: "))

#Count digits of number
count = 0
tempNum = num1
temp2 = num1
summ = 0
while (num1 > 0):
    num1 = num1 // 10
    count += 1

while (tempNum > 0):
    divisor = tempNum % 10
    summ = summ + pow(divisor, count)
    tempNum = tempNum // 10

if summ == temp2:
    print("Armstrong number")
else:
    print("Not a armstrong number")


