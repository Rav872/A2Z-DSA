rows = int(input("Enter number of rows: "))
spaces  = 0
for i in range(1, rows+1):
    if i == 1 or i == rows:
        print("*" * rows)
    else:
        spaces = rows-2
        stars = rows - spaces
        print("*" * (stars//2) + " " * spaces + "*" * (stars//2))