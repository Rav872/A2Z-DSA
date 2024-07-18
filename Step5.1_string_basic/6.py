# Check if string is rotated or not
p = "ABCD"
q = "CDAB"
charIndex = p.index(q[0])
lenP = len(p)
flag = True
for c in q:
    if c != p[charIndex]:
        flag = False
        break
    if charIndex < lenP-1:
        charIndex += 1
    else:
        charIndex = lenP - charIndex - 1
        
if flag:
    print("Yes: string is rotated")
else:
    print("No: string is not rotated")