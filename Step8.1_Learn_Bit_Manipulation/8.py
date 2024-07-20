# Toggle all bits
# 0000 0000  0000 1110
# 1111 1111  1111 1111

# 1111 1111  1111 0001

# 1111 1111  1111 0001


def toggleAllBits(N):
    return ~N

N = 25

print(bin(N))

print(bin(toggleAllBits(N)))