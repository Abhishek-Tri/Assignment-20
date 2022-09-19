"""Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters."""

def upperLower(s):
    c1,c2=0,0
    for e in s:
        if ord(e)>=65 and ord(e)<=90:
            c1+=1
        elif ord(e)>=97 and ord(e)<=122:
            c2+=1
    print("number of upper case letters:",c1) 
    print("number of lower case letters:",c2)  

upperLower(input("Enter a string: "))       
