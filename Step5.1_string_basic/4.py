# Longest common prefix
 
words = ["Apple", "Appp", "App", "Appl]
 
minLen = 99999
temp = ""
for word in words:
    if len(word) < minLen:
        minLen = len(word)
        temp = word
 
flag = True
for word in words:
    if temp not in word:
        flag = False
        break
if flag:
    print("Longest common prefix is: ", temp)
else:
    print("No longest common prefix")