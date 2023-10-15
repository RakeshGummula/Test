'''1.Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}'''

# Dictionary={0:10,1:20}
# print(Dictionary)
# Dictionary.update({2:30})
# print(Dictionary)

#           *2.Write a Python script to check whether a given key already exists in a dictionary.*

# Dictionary = eval(input("Enter a dictionary: "))
# Key = eval(input("Enter a key to check: "))
# if Key in Dictionary:
#     print("Yes Present")
# else:
#     print("Not Present")

#           *3.Write a Python program to iterate over dictionaries using for loops*
# dictionary = {}
# numberof = int(input("Enter the number of key-value pairs: "))
# for i in range(numberof):
#     key = input("Enter the key " + str(i+1) + ": ")
#     value = input("Enter the value " + str(i+1) + ": ")
#     dictionary[key] = value
# print("The dictionary is: ", dictionary)
# for k, v in dictionary.items():
#     print(k, v)

'''4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}'''
# dictionary={d: d**2 for d in range(0,16)}
# print(dictionary)

'''5.Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'marolix technology'
Expected output: {'m': 1, 'a': 1, 'o': 3, 'l': 2, 'i': 1, 'x': 1, 't': 1, 'e': 1,'c': 1, 'h': 1, 'n': 1, 'g': 1,'y':1}'''
# String=input("Enter a String : ")
# Dictionary={}
# for char in String:
#     if char in Dictionary:
#         Dictionary[char]+=1
#     else:
#         Dictionary[char]=1
# print(Dictionary)

#           *6. Write a Python program to sum all the items in a dictionary.*
# mydictionary={}
# numberof=int(input("how many want to add : "))
# for i in range(numberof):
#     key=input(f"enter a key for item {i+1} : ")
#     value=eval(input(f"enter a value for item {i+1} : "))
#     mydictionary[key]=value
# total=0
# for key,value in mydictionary.items():
#     total+=value
# print(f"dictionay is : {mydictionary}")
# print(f"Sum of all values is : {total}")

'''7.Write a Python program to combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})'''
dictionary1=eval(input("enter Dict1 key values : "))
dictionary2=eval(input('enter Dict2 key values : '))
