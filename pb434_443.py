# Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using
# lambda function.
l=[1,2,3,-1,-2,0]
pos=sum(filter(lambda x:x>0,l))
neg=sum(filter(lambda x:x<0,l))
print(pos,neg)             
