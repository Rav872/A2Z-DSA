# Two number with odd occurrences

R = [2,4,1,3,2,4]

xor = 0

for i in range(len(R)):
    xor ^= R[i]            # xor all elements

# Find the rightmost set bit in xor result

for i in range(32):
    if xor >> i & 1:
        setPosition = i 
        break

firstUnique = 0
secondUnique = 0


for i in range(len(R)):
    if R[i] >> setPosition & 1:
        firstUnique ^= R[i]
    else:
        secondUnique ^= R[i]

print("First Unique: ", firstUnique, "Second Unique: ", secondUnique)