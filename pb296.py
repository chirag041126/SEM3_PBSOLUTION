# write a python code remove I'th character from string
s="Chiku"
r=""
x=input("enter character and remove=")
if x in s:
    index=s.index(x)
    r=s[0:index]+s[index+1:]
else:
    print("element is not found")
print(r)