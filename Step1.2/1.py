row = int(input("Enter the rows: "))
column = int(input("Enter the columns: "))

for r in range(row):
    for c in range(column):
        print("*", end="")
    print("\n", end="")