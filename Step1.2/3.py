row = int(input("Enter the rows: "))

for r in range(row):
    for c in range(r+1):
        print(c+1, end="")
    print("\n", end="")

