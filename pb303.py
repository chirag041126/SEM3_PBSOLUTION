# write a python code to capitalize the first and last character of each word in string
s="i love you kiara advani"
y=s.split() 
z=""
for i in y:
    if len(i)==1:
        z=z+i[0].upper()+" "
    else:
         new=i[0].upper()+i[1:-1]+i[-1].upper()
         z=z+new+" "
print(z)    
# output:I LovE YoU KiarA AdvanI