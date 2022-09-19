#Write a python program to create a function to find the Min of three numbers.

def findmin(n1,n2,n3):
    if n1<n2:
        if n1<n3:
            print(n1 ,"is smallest")
    elif n2<n3:
        print(n2, "is smallest")
    else:
        print(n3 ,"is smallest")          

#function calling
findmin(int(input("Enter first number:")),int(input("Enter second number:")),int(input("Enter third number:")))     
