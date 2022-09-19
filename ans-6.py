"""Write a python program to create a function and print a list where the values are
square of numbers between 1 and 30."""

def PrintSqrList():
    l1=[]
    for e in range(1,31):
        l1.append(e**2)
    return l1

print("list of squares is :",PrintSqrList())        