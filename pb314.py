# Input Text : LJIET ENG
# Shift : 3
# Cipher: OMLHW HQJ
s=input("enter string:")
shift=int(input("enter shift:"))
alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
z=""
s=s.upper()
for i in s:
    if i in alph:
        index=(alph.find(i)+shift)%26
        z=z+alph[index]
    else:
        z=z+i
print(z)        
