# write a python code if a string is pallindrome or not.
s=input("Enter string=")
if s[0::]==s[::-1]:
    print("string is pallindrome")
else:
    print("string is not pallindrome")   