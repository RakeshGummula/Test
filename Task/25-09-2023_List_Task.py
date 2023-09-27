#            *1.write a python program to merge two lists.*
            #1#
# list1=input("Enter a list1 : ").split()
# list2=input("Enter a list2 : ").split()

# for i in list2:
#     list1.append(i)

# print("concatenated list : ",list1)

                #2#
# list3=input("Enter a list3 : ").split()
# list4=input("Enter a list4 : ").split()

# list3.extend(list4)
# print(list3)


#           *2.write a python program to find the sum of list elements.*

            #1#
# list5=input("Enter a list (space-separated): ").split()
# list5=[int(item) for item in list5]
# total=sum(list5)
# print("sum of list :",total)

            #2#

# numbers=eval(input("Enter a list numbers : "))
# total=0
# for num in numbers:
#     total+=num
# print("Sum of numbers :",total)

#               *3.write a python program to print even and odd numbers seperatly in list.*
            #1#
# numlist = input("enter a list of numbers :").split()
# numblist=[int(lst) for lst in numlist]
# evenlist=[]
# oddlist=[]
# for j in range(len(numblist)):
#     if numblist[j] % 2 !=0:
#         oddlist.append(numblist[j])
#     else:
#         evenlist.append(numblist[j])

# print("Odd numbers :",oddlist)

# print("Even numbers :",evenlist)

        #2#

# oddeven=eval(input("Enter a list of numbers :"))
# print("Evenumbers are:",oddeven[1:100:2])
# print("Oddnumbers are :",oddeven[0:100:2])

#               *4.write a python program to delete element of given index in list.*

                #1#
# listelements=eval(input("Enter a list of numbers :"))
# indextodel=int(input("Enter an index to delete :"))
# if 0<=indextodel<len(listelements):
#     del listelements[indextodel]
# else:
#     print("Invalid Index list cannot be changed")
# print("Modified List : ",listelements)

                #2#
# elementslist=input("Enter a list of numbers :").split()
# elementslists=[int(item)for item in elementslist]
# delindex=int(input('Enter index to delete : '))
# if 0<=delindex<len(elementslists):
#     elementslists=elementslists[:delindex]+elementslists[delindex+1:]
# else:
#     print("Invalid Index list remains  unchanged")

# print("Modified List : ",elementslists)

#                       *5.write a python program to delete given element from the list *
                #1#
# numbers=eval(input("Enter a numbers of list : "))
# element=eval(input('Enter a element to delete : '))
# if element in numbers:
#     numbers.remove(element)
#     print("Updated List is : ",numbers)
# else:
#     print("Element not in list")

                #2#

# numbers=input("Enter a elements of numbers : ").split()
# numbers1=[int(item) for item in numbers]
# element=int(input("enter elements to delete : "))
# numbers1.remove(element)
# print(numbers1)

#                       *6.write a python program to insert an element  at given index location.*

                #1#
# element=eval(input('Enter a elements of List : '))
# element.insert(eval(input('Enter index number to add : ')),eval(input('enter a element to add : ')))
# print("List after modified :",element)

                #2#
# new_list=[]
# n = int(input("Enter the number of elements in the list: "))
# for i in range(n):
#     element = input(f"Enter element {i+1}: ")
#     new_list.append(element)
# print(f"The original list is: {new_list}")
# index = int(input("Enter the index to insert an element: "))
# element = input("Enter the element you want to insert: ")
# new_list.insert(index, element)
# print(f"The updated list is: {new_list}")


#                       *7.write a python program to check the sizes of given two lists are same.*
                #1#
# number=int(input("Enter a number of elements in 1 list : "))
# list1=[]
# for i in range(number):
#     element=input(f"Enter a element {i+1} for the 1 list : ")
#     list1.append(element)

# number1=int(input("enter number of elements of 2 list : "))
# list2=[]
# for i in range(number1):
#     element1=input(f"Enter elements {i+1} for 2 list : ")
#     list2.append(element1)

# if len(list1) == len(list2):
#     print("the sizes of 2 list are same.")
# else:
#     print('The sizes of 2 lists are not same ')

                #2#
# list1=[]
# list2=[]
# print("enter elements for 1 list. enter 'exit' if done: ")
# while True:
#     element=input("Enter an element : ")
#     if element == "exit":
#         break
#     else:
#         list1.append(element)
# print("enter elements for 2 list. enter 'exit' if done : ")
# while True:
#     element1=input("enter an element : ")
#     if element1 == "exit":
#         break
#     else:
#         list2.append(element1)
# size1=0
# for item in list1:
#     size1+=1
# size2=0
# for item in list2:
#     size2+=1
# if size1 == size2:
#     print("Sizes of both lists are same. ")
# else:
#     print("Sizes of both lists are not same. ")

#               *8.Write a Python function that takes two lists and returns True if they have at least one common member.*
                #1#
# list1=eval(input("enter a list1 : "))
# list2=eval(input("enter a list2 : "))
# common=0
# for elements in list1:
#     if elements in list2:
#         common=1
# if common==1:
#     print("True")
# else:
#     print('False')

                #2#
# list1=input("enter a 1 list : ").split()
# list2=input("enter a 2 list : ").split()
# list1=[eval(r) for r in list1]
# list2=[eval(a) for a in list2]
# common=False
# for item1 in list1:
#     for item2 in list2:
#         if item1 == item2:
#             common=True
#             break
# if common:
#     print("List have one common elements : ")
# else:
#     print("List doesn't have common elements : ")       

''' 9.Write a Python program to remove a specified column from a given nested list.
Original Nested list:
[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
After removing 1st column:
[[2, 3], [4, 5], [1, 1]] '''

                #1#
# list1=eval(input("enter a nested list :"))
# for row in list1:
#         del row[0]
# print("After removing 1st column :", list1)

                #2#
# nestedlist=eval(input("Enter a nested list : "))
# column=int(input("enter column to delete from 0 to n :"))
# result=[]
# for row in nestedlist:
#     row1=row[:]
#     row1.pop(column)
#     result.append(row1)
# print("original nested List : ",nestedlist)
# print('After removing 1 column :',result)

'''10. Write a Python program to convert a list of multiple integers into a single integer.
Sample list: [11, 33, 50]
Expected Output: 113350'''

                #1#
# Samplelist=eval(input("enter a list : "))
# newlist=[str(me) for me in Samplelist]
# print("".join(newlist))

                #2#
# list1=eval(input('enter a list : '))
# for i in list1:
#     print(i,end="")

#               *11.Write a Python program to remove duplicates from a list.*
                #1#
# new_list=eval(input("enter a list : "))
# new_list1=[new_list [i] for i in range(len(new_list)) if new_list.index(new_list[i])==i]
# print(new_list1)

                #2#
# my_list=eval(input("enter a list : "))
# my_list1=list(dict.fromkeys(my_list))
# print(my_list1)