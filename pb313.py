#  input of “Mr. Ed” will result in “mR. eD” as the output string
s="mr. Chiku"
z=""
for i in s:
    if i.isupper():
        z=z+i.lower()
    else:
        z=z+i.upper()
print(z)   
#output=MR. cHIKU  