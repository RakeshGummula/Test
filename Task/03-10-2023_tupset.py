#           *1.Write a Python program to unpack a tuple into several variables.*

# training=("Marolix",1000,'hyderabad',"Python")
# (company,employees,location,domain)=training
# print("company name : ",company)
# print('no.employees :',employees)
# print("Location from working : ",location)
# print('job domain : ',domain)

#           *2.Write a Python program to add an item to a tuple.*

# excersize=(eval(input("enter any items : ")))
# excersize=list(excersize)
# excersize.append(eval(input("enter anything want to add : ")))
# print(excersize)
# excersize=tuple(excersize)
# print(excersize)

'''                 3.Write a Python program to convert a tuple to a string.
                        Ex:tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')'''

# tuples = (eval(input("enter any items : ")))
# mytuple=''.join(tuples)
# print(mytuple)

#           *4.Write a Python program to get the specified element from the last element of a tuple.*

# elements=(eval(input("enter any items : ")))
# print(elements[eval(input("enter element index need to get : "))])

#          *5.Write a Python program to add member(s) to a set.*

# setelement=eval(input("enter an elements of set : "))
# setelement.add(eval(input("enter elements need to Add : ")))
# print(setelement)

#               *6.Write a Python program to create an intersection of sets.*

# set1=eval(input("Enter a set1 : "))
# set2=eval(input('enter a set2 : '))
# print(set1.intersection(set2))
# print(set1 & set2)

#                   *7.Write a Python program to create a union of sets.*

# set3=eval(input("enter an Set3 items : "))
# set4=eval(input('enter an set4 items : '))
# print(set3.union(set4))
# print(set3 | set4)

#                   *8.Write a Python program to create set difference.*

# set5=eval(input("enter an set5 items : "))
# set6=eval(input('enter an set6 items : '))
# print(set5.difference(set6))
# print(set5 - set6)

#                   *9.Write a Python program to create a symmetric difference.*

# set7=eval(input("enter an set7 items : "))
# set8=eval(input('enter an set8 items : '))
# print(set7.symmetric_difference(set8))
# print(set7^set8)

#                       *10.Write a Python program to find the maximum and minimum values in a set.*

# maxmin=eval(input("enter an set items to find max-min : "))
# print(max(maxmin))
# print(min(maxmin))