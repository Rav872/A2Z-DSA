# Find the number which occurs odd number of times

N = [4,5,6,5,6,9,9,4,4]
xor = 0
for i in range(len(N)):
    xor ^= N[i]

if xor == 0:
    print("No number occurred odd number of times")
else:
    print("Odd number of times occurred: ", xor)
