s=" Don’t wait for your feelings to change to take the action. Take the action and your feelings will change"
d={}
y=s.split()
for i in y:
    d[i[0]]=d.get(i[0],[])
    d[i[0]].append(i)
print(d)