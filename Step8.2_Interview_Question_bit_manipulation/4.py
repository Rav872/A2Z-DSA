# Find xor number from L to R

def xorOffirstN(N):
    if N % 4 == 1:
        return 1
    if N % 4 == 2:
        return N + 1
    if N % 4 == 3:
        return 0
    if N % 4 == 0:
        return N



L = 12
R = 34

print("xor of L to R: ", xorOffirstN(R) ^ xorOffirstN(L-1))