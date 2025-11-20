l=['abc','xyz','aba','2112','123451','12345']
count=0
for i in l:
    if len(i)>=3 and i[0]==i[-1]:
        count+=1
print(count) 