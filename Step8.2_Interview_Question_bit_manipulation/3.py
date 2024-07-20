# Power set using bitwise operation

def iterate(string, s):
    temp = ""
    for i in range(len(string)):
        if string[i] == '1':
            temp += s[i]
    return temp


s = "deepak"

length = len(s)

power = pow(2, length)

for i in range(power):
    binary = format(i, '0{}b'.format(length))
    string = iterate(binary, s)
    print(string, end=" ")