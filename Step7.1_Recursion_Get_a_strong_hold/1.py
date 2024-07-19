#Recursive implementation of atoi

def atoi(s, result= ''):
    if not s:
        return result
    digit = ord(s[0]) - ord('0')
    if 0 <= digit <= 9:
        result += str(digit)
    return atoi(s[1:], result)


s = "46rk59"  
print(atoi(s))