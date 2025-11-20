x=[4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
d={}
for i in x:
    d[i]=d.get(i,[])
    d[i].append(i)
z=dict(sorted(d.items(),key=lambda x:len(x[1]),reverse=True))
print(z)