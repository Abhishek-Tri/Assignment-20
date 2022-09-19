"""Write a python program to create a function that checks whether a passed string is palindrome or not."""

def checkPdrome(s):
    l1=list(s)
    l2=[]
    for e in l1:
        l2.insert(0,e)
    if l1==l2:
        print("String",s,"is palindrome")
    else:
        print("String",s,"is NOT palindrome")

        
checkPdrome(input("Enter a String :"))    