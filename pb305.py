# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.
s1="abc"
s2="abcd"
for i in s1:
    if i not in s2:
        print("s1 and s2 are not balanced")
        break
else:
    print("s1 and s2 are balanced")    
#output=s1 and s2 are balanced