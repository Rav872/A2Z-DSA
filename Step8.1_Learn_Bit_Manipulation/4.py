# check if a number is power of two or not
 
def checkIfNumberIsPowerOfTwo(N):
    if N & (N-1) == 0:
        print("Number is power of two")
    else:
        print("Number is not a power of two")
 
 
N = 15
 
checkIfNumberIsPowerOfTwo(N)