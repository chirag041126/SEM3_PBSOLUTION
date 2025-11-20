s="Dog the quick brown fox jumps over the lazy dog"
y=s.lower()
y=y.split()
d={}
for i in y:
    d[i]=y.count(i)
print(d)  


