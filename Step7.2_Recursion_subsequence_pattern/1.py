def isBinValid(val):
    s = str(val)
    print("string is : ", s)
    for i in range(len(s)-1):
        if s[i] == '1' and s[i+1] == '1':
            return False
    return True

def binaryStringCalculate(N, desiredDigit, count=0):
    if N < 0:
        return count
    else:
        val = format(N, '0{}b'.format(desiredDigit))
        if isBinValid(val):
            count += 1
        return binaryStringCalculate(N-1, desiredDigit, count)

N = int(input("Enter the value of N: "))
desiredDigit = N
N = pow(2, N) - 1
count = binaryStringCalculate(N, desiredDigit)
print("Number of counts are: ", count)