s="chiku12345"
sum=0
count=0
for i in s:
    if i.isdigit():
        sum=sum+int(i)
        count+=1
if count>0:
    print(f"Sum of digit={sum}")
    print(f"AVG={sum/count}") 
else:
    print("No digit found")           
# output sum of digit=15 & AVg=3