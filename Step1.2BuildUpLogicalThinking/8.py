row = int(input("Enter the rows: "))
for r in reversed(range(row)):
    print((row-r+1)*" " + "*" * (r*2+1) + (row-r+1)*" ")