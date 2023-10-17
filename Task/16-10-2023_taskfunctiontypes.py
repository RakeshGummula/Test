# map()
    #1#
# number1=eval(input("enter number for list : "))
# number2=eval(input('enter numbers for list : '))
# result=map(lambda x,y : x*y,number1,number2)
# print(result)
# print(list(result))
        #2#
# mylist=input("enter a list : ").split()
# mylist=[eval(x) for x in mylist]
# updated=map(round,mylist)
# print(updated)
# print(list(updated))

# lambda()
    #1#
# string=input('enter a string : ')
# upper=lambda string:string.upper()
# print(upper(string))
    #2#
# MAX=lambda a,b : a if (a>b) else b
# print(MAX(14,6))

# reduce()
    #1#
# from functools import *
# number=int(input("enter a number : "))
# factorial=reduce(lambda x,y : x*y, range(1,number+1))
# print(factorial)
        #2#
# from functools import *
# numbers=eval(input("enter a list of numbers : "))
# max_num=reduce(lambda x,y:x if x>y else y,numbers)
# print(max_num)

# nestedfunction
        #1#
# def function1():
#     sample=input("Enter some text here : ")
#     def function2():
#         print(sample)
#     function2()
# function1()
        #2#
# def outerfunction(text):
#     text=text
#     def innerfunction(text):
#         print(text)
#     innerfunction()

# filter()
        #1#
# sequence=eval(input("enter a list numbers : "))
# result=filter(lambda x : x%2!=0,sequence)
# print(list(result))
# result=filter(lambda x : x %2==0,sequence)
# print(list(result))
        #2#
# def multiples(number):
#     return number % 3==0
# numbers=eval(input("enter a number of list : "))
# result=list(filter(lambda x: multiples(x),numbers))
# print(result)

# recursive
