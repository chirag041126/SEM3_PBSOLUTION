l=[2,4,6,8]
j=len(l)-1
i=1
while(i<=j):
    x=l.pop(j)
    l.insert(i,x)
    i+=2
print(l)