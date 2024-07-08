rows = int(input("Enter number of rows"))

start = 1
for r in range(1, rows+1):
    start = ((r*(r-1))//2) + 1
    for c in range(r):
        print(start, end="")
        start = start+1
    print("\n", end="")
