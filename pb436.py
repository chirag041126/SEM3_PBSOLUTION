#Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda
l=[1,38,2,4]
d=list(filter(lambda x:(x%13==0)or(x%19==0),l))
print(d)