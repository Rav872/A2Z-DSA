# set the right most bit
 
def UnsetRightMostSetBit(N):
    return N & (N+1)
 
def setRightMostUnsetBit(N):
    return N | (N+1)          # N+1 make first 0 as 1
 
N = 54
print(bin(N))
 
print(bin(setRightMostUnsetBit(N)))
 
print(bin(UnsetRightMostSetBit(N)))