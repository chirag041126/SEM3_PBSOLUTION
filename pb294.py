#find calculate  of string uppercase and lowercase letter
s="ChiKu"
upper=0
lower=0
for i in s:
    if i.isupper():
         upper=upper+1
    else:
         lower=lower+1
print("uppercase letter",upper)
print("lowercase letter",lower)                  
