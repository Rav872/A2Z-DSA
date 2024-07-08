row = int(input("Enter the rows: "))

for r in reversed(range(1,row+1)):
    for c in range(1,r+1):
        print(c, end="")
    print("\n", end="")