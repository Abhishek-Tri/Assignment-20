#Write a python program to create a function to check whether a string is an anagram or not

def anagram(s1,s2):
    for i in s2:
        if i not in s1:
            print("string",s1,"and",s2,"are NOT anagram strings")
            break
    else:
        print("string",s1,"and",s2,"are anagram strings")    



anagram(input("Enter first string :"),input("Enter second string :"))    