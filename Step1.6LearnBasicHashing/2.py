number = []
 
for i in range(10):
    number.append(i)
 
number.append(1)
number.append(8)
number.remove(0)
 
print(number)
 
minn = min(number)
maxx = max(number)
 
print(minn, " ", maxx)
 
print(number.count(minn))
print(number.count(maxx))