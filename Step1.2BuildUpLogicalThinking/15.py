rows = int(input("Enter the number of rows: "))

for i in reversed(range(rows)):
    for c in range(i+1):
        start = chr(65 + c)
        print(start, end="")
    print("\n", end="")