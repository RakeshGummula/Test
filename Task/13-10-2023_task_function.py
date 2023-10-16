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
list1=eval(input("enter an list items : "))
def unique(list1):
    unique_list=[]
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print("the Unique Values are : ",x)
unique(list1)