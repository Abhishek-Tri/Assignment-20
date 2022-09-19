#Write a python program to create a function that takes a number as a parameter and
#checks if the number is prime or not.

def primecheck(n):
    for i in range(2,n,1):
        if n%i==0:
            print(n ,"is not prime number")
            break
    else:
        print(n ,"is a prime number")
       
primecheck(int(input("Enter a number :"))) 

      