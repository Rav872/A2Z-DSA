# check if number is prime

num = int(input("Enter a number: "))

if num < 2:
    print("Not a prime number")
    exit

check = True
for i in range(2, num):
    if num % i == 0:
        print("Not a prime number")
        check = False
        break

if check:
    print("Prime Number")
    
