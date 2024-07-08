row = int(input("Enter the rows: "))

for r in range(row):
    print((row-r+1)*" " + "*" * (r*2+1) + (row-r+1)*" ")
for r in reversed(range(row)):
    print((row-r+1)*" " + "*" * (r*2+1) + (row-r+1)*" ")

print("...........")
# Try using one loop
num = (row * 2) - 1

for i in range(1, num+1):
  i = i - (num//2 +1)
  if i < 0:
    i = -i
  print(" " * i + "*" * (num - i*2) + " "*i)