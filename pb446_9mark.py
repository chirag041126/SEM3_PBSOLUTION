pw=input("Enter password:")
u=0
l=0
d=0
e=0
s=0
if 15>=len(pw)>=8:
    for i in pw:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
        elif i.isdigit():
            d+=1
        elif i.isspace():
            s+=1
        else:
            e+=1
    if u>=1 and l>=1 and 3>=d>=1 and s==0 and e>=1:
        print(f"pw={pw}")
        print("valid password.")   
        num=0                 
        for i in pw:
            if i.isdigit():
                num=num*10+int(i)
        print(f"num={num}")
        dictionary={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Ninteen",20:"Twenty",30:"Thirty",40:"Fourty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninty",100:"Hundreed"}
        def abc(num):
            if num<=20:
                return dictionary[num]
            if num<100:
                if num%10==0:
                    return dictionary[num]
                else:
                    return dictionary[num//10*10]+"-"+dictionary[num%10]
            if num<1000:
                if num%100==0:
                    return dictionary[num//100]+"-"+"Hundread"
                else:
                    return dictionary[num//100]+"-"+"Hundread-"+abc(num%100)
        print(abc(num))                    
    else:
        print("Invalid password.")
else:
    print("Invalid password")
        