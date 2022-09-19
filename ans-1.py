"""Write a python program to create a function that takes a list and returns a new list
with the original list's unique elements"""

def returnunq(l1=[]):
    s1=set(l1) 
    l1=list(s1)
    return l1

list1=[1,1,2,2,3,3,4,4,5,5]
print("original list is :",list1)
print("returned unique list is :",returnunq(list1))
