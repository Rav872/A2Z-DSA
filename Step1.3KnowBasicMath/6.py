#print all divisors

num1 = int(input("Enter a number: "))

for i in range(1, num1):
    if num1 % i == 0:
        print(i, end=" ")