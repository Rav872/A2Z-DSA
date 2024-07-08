rows = int(input("Enter the number of rows: "))

for i in range(rows):
    start = chr(65 + i)
    for c in range(i+1):
        print(start, end="")
    print("\n", end="")