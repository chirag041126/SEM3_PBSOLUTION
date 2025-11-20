# Write a program to print sum of even numbers and sum of odd numbers from elements given in tuple.
t=(1,2,3,4,5,6,7)
even=0
odd=0
for i in t:
    if i%2==0:
        even+=i
    else:
        odd+=i
print("even number sum=",even)
print("odd number sum=",odd) 
#output=even number sum= 12
    #   odd number sum= 16    