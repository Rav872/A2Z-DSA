# count the number of set bits
 
def countNumberOfSetBits(N):
    count = 0
    while N:
        count += N & 1
        N >>= 1
    return count
    
 
N = 35
print(bin(N))
 
count = countNumberOfSetBits(N)
 
print("Number of set bits are: ", count)