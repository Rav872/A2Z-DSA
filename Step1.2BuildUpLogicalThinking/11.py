
rows = int(input("Enter number of rows: "))

start = 1
for r in range(rows):
    if r % 2 == 0:
        start = 1
    else:
        start = 0
    for c in range(r+1):
        print(start, end="")
        start = 1 - start
    print("\n", end="")