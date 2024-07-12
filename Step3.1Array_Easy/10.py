# Find a missing number from 1 to N

my_list = [1,2,3,4,5,6,8,9]
num = int(input("Enter value of N: "))

totalSum = (num * (num + 1))//2
arraySum = 0
for i in my_list:
    arraySum += i

print("Missed number is: ", totalSum - arraySum)

# Another way is find if difference of two consective element is more that 1
