from collections import Counter
words = ["abba","baba","bbaa","cd","cd"]
l = []
for i in words:
    l.append(''.join(sorted(i)))

d = Counter(l)
s = [d.keys()]
print(s)