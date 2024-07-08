row = int(input("Enter the rows: "))

for r in range(row):
    print("*" * (r*2+1) + (row-r+1)*" ")
for r in reversed(range(row-1)):
    print("*" * (r*2+1) + (row-r+1)*" ")