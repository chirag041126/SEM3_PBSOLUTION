n="123456"
shift=int(input("Enter shift="))
if shift>len(n):
    print(n[::-1])
else:
    ans=n[shift:]+n[0:shift] 
    print(ans)
