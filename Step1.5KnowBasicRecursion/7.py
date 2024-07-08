# Check if a string is palindrome or not
def IfPalindrome(firstIndex, lastIndex, size, name):
    
    if firstIndex == size//2 - 1:
        return True
    elif name[firstIndex] != name[lastIndex]:
        return False
    else:
        return IfPalindrome(firstIndex + 1, lastIndex - 1, size, name)
    
 
name = input("Input name: ")
firstIndex = 0
size = len(name)
lastIndex = size - 1
 
if IfPalindrome(firstIndex, lastIndex, size, name):
    print("Palindrome!")
else:
    print("Not a Palindrome!")