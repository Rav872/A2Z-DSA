
def isGoodNumber(num):
    lastDigit = -99999
    totalSum = 0
    firstDigit = True
    while num > 0:
        digit = num % 10
        if not firstDigit:
            if digit <= totalSum:
                return False
        num = num // 10
        totalSum += digit
        firstDigit = False
    return True
        

def countGoodNumbers(a,b, count=0):
    if a > b:
        return count
    else:
        if isGoodNumber(a):
            count += 1
    return countGoodNumbers(a+1, b, count)

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("Good numbers are: " , countGoodNumbers(a,b))