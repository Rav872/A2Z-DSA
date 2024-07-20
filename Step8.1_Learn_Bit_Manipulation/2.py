# check if ith bit is set or not
 
 
def checkIfithBitSet(N, i):
    return (N >> i) & 1
 
N = 25  # 11001
i = 3 # 0 based indexing
 
print(checkIfithBitSet(N,i))