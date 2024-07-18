#Create atoi
# consider only numeric value, ignore all other values
 
s = "-546+er"
negativeFlag = False
if s[0] == '-':
    negativeFlag = True
 
output = ""
for c in s:
    if c >= '0' and c <= '9':
        output += c

if negativeFlag:
    output = "-"+output
    
print(output)