x=input("set password:")
e=0
l=0
u=0
d=0
s=0
if len(x)<8:
    print("invalid password")
else:
    for i in x:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
        elif i.isdigit():
            d+=1
        elif i.isspace():
            s+=1
        else:
            e=e+1
    if (e>=1 and  u>=1 and l>=1 and d>=1 and s<1):
        print("valid password:")
    else:
        print("invalid password")                  