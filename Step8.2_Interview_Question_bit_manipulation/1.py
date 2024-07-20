
def numberOfBitsFlipped(A,B):
    count = 0
    while A or B:
        if (A & 1) != (B & 1):
            count += 1
        B >>= 1
        A >>= 1
    return count
A = 11
B = 18

print("Number of bits flipped to be needed:" , numberOfBitsFlipped(A,B))