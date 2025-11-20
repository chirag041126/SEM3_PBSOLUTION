# Write a program to Create a string made of the middle three characters
s="solanki"
length=len(s)
if length>=3:
    mid=length//2
    result=s[mid-1:mid+2]
    print("middle three character:",result)
else:
     print("string is too short")
#output:lan  