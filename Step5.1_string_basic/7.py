# Check if string is anagram or not
# anagram is count of characters in both strings should be equal
 
p = "RULES"
q = "LESRT"
 
if len(p) != len(q):
    print("strings are not anagram")
else:   
    c = 0
    flag = True
    while c < len(p):
        if p.count(p[c]) != p.count(q[c]):
            flag = False
            break
        c += 1
 
    if flag:
        print("Anagram!")
    else:
        print("Not anagram")