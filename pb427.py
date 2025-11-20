# Write a Python Program to print the largest even number in a list. 
l=[1,2,4,5,6,7]
s=[]
for i in l:
    if i%2==0:
        s.append(i)
print("largest even number in a list",max(s))        

