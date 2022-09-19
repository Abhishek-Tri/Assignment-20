#Write a python program to create a function to check whether a string is a pangram or not.

def pangramStr(s):
    c=0
    for e in s:
        if (ord(e)>=65 and ord(e)<=90) or (ord(e)>=97 and ord(e)<=122):
            c+=1                    
    if c==26:
        print("String is Pangram string")
    else:
        print("String is NOT Pangram String")    


pangramStr(input("Enter a string :"))
