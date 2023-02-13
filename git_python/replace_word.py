import re

str = '''Python uses duck typing and has typed objects but untyped variable names. Type constraints are not checked at compile time; rather, operations on an object may fail, signifying that it is not of a suitable type. Despite being dynamically typed, Python is strongly typed, forbidding operations that are not well-defined (for example, adding a number to a string) rather than silently attempting to make sense of them.'''

#WORD COUNT:-

print()

print(str)

a = str.split(" ")

word = input("\nPlease Enter a Word You Want to Find an Occurance : ")

def count_word(string,word):
    count = 0
    for i in range (0,len(a)):
        if word == a[i]:
            count = count + 1 
    return count

print(f'\nThe occurance of the {word} is {count_word(a,word)}')


#REMOVE THE WORD :-

delete_word = input("\nEnter a word to delete : ")

str = re.sub(delete_word,"", str)

print()

print(str)


# TO ADD THE STRING IN THE START AND END OF THE TEXT. 

our_string = str

print()

start_string = input("Please enter the string to add in the starting of the existing string : " )

print()

end_string = input("Please enter the string if you want to add in the end of our given string : ")

print()

modified_string = (start_string)+(str)+(end_string)

print(modified_string,end='')

print()

#reverse a string 

rev_string = input("Enter a string which you wanted to reverse : ")

def reverse(s):
    modify = ' '
    for i in s:
        modify = i + modify
    return modify

re = reverse(rev_string)
print(re)
        
