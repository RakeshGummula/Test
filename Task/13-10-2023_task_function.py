'''1.Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12'''

# def numberof(string):
#     uppercount=0
#     lowercount=0
#     for char in string:
#         if char.isupper():
#             uppercount+=1
#         elif char.islower():
#             lowercount+=1
#     return(uppercount,lowercount)
# string=input("enter a string : ")
# count=numberof(string)
# print(f"No. of uppercase characters : {count[0]}")
# print(f"No. of Lowercase characters : {count[1]}")

'''2.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]'''

# list1=eval(input("enter an list items : "))
# def unique(list1):
#     unique_list=[]
#     for x in list1:
#         if x not in unique_list:
#             unique_list.append(x)
#     print('The Unique List is :',unique_list)
# unique(list1)

'''3.Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog".'''

# string = input("enter a string : ")
# def is_panagram(string):
#     string=string.lower()
#     string="".join(c for c in string if c.isalpha())
#     letters=set(string)
#     return len(letters)==26
# result=is_panagram(string)
# if result:
#     print('the string is panagram')
# else:
#     print("the string is not panagram")

'''4.Write a Python function to create and print a list where the values are the squares of 
numbers between 1 and 10 (both included).'''

# def list1():
#     new_list=[]
#     for i in range(1,11):
#         new_list.append(i*i)
#     return new_list
# new_list=list1()
# print(new_list)

'''5.Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20'''

# number=eval(input("enter a list numbers: "))
# total =0
# for x in number:
#     total+=x
# print("sum of all : ",total)

'''6.write a function to find sum of given values, pass values has variable number of arguments to function.'''
# def addition(*args):
#     total=0
#     for arg in args:
#         total+=arg
#     return total
# values=input("enter values comma seperated : ")
# values=[int(x) for x in values.split(",")]
# completed=addition(*values)
# print('sum of arguments :',completed)
