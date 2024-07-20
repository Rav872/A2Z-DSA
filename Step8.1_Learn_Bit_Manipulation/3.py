# check if a number is odd or not
 
def checkIfNumberIsOdd(N):
    if (N & 1) != 0:
        print("N is odd")
    else:
        print("N is even")
 
N = 457
 
checkIfNumberIsOdd(N)