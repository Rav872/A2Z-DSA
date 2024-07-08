rows = int(input("Enter number of rows:"))

#Upper Half
for i in range(rows):
    spaces = 2 * i
    stars = (2*rows) - spaces
    print("*" * (stars//2) + " " * spaces + "*" * (stars//2))
#Lower Half
for i in reversed(range(rows)):
    spaces = 2 * i
    stars = (2*rows) - spaces
    print("*" * (stars//2) + " " * spaces + "*" * (stars//2))