#Write a Python program to rearrange positive and negative numbers in a given array using Lambda
arr=[1,-7,-4,3,2,-10,5,-2]
positive=list(filter(lambda x:x>0,arr))
negetive=list(filter(lambda x:x<0,arr))
result=positive+negetive
print(result)