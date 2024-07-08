word = input("Enter any word: ")

reversedWord = ""

for char in word:
    reversedWord = char + reversedWord

if word == reversedWord:
    print("Palindrome!")
else:
    print("Not palindrome!")