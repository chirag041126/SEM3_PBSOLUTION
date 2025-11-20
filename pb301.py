# write a python code to print even length words in string
s="I LOVE you SO much"
y=s.split()
for i in y:
    if len(i)%2==0:
        print(i,end=" ")
#output: LOVE SO much 
