rows = int(input("Enter the number of rows: "))

#Upper half
for i in range(1,rows+1):
    spaces = 2*(rows - i)
    stars = 2*rows - spaces
    print("*" * (stars//2) + " " * spaces + "*" * (stars//2))

#lower half
for i in reversed(range(1, rows)):
    spaces = 2*(rows - i)
    stars = 2*rows - spaces
    print("*"*(stars//2) + " " * spaces + "*" * (stars//2))