# Sort characters by frequency
s = "aaBbbceddf"
sett = set(s)
freq = {}
result = ""
maxFreq = len(s)
for c in sett:
    freq[c] = s.count(c)

