#Write a python program to access a function inside a function.

def printbin(no):
    return bin(no)

def printoctal(n):
    r=printbin(n)  
    print("binary of",n,"is:",r)
    print("octal of",n,"is:",oct(n))

printoctal(int(input("Enter a number :")))      