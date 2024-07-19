
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

x = float(input("Enter the x: "))
n = int(input("Enter the power: "))

print(round(power(x,n),2))