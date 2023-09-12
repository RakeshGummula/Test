#           *if elif else Example with user input*

# price = int(input("Enter Price:"))
# if price > 100:
#     print("price is greater than 100")
# elif price == 100:
#     print("price is 100")
# else :    
#     print("price is less than 100")

#           *for loop Example with user input*

# me = str(input("Enter a string: "))
# for char in me:
#     print(char)

#           *Break Example*

# for i in numbers:
#     if i == 6:
#         break
#     print(i)

#           *Continue Example*

# for i in range(11,20):
#     if i == 17:
#         continue
#     print(i)

#           *Pass Examples*

# for m in [9,7,4]:
#     pass

#       *While Loop Examples*

# i = 0
# while i < 8:
#     print(i)
#     i+=1
# else:
#     print("i is no longer than 8")

#   *Break Example User input*

# while True:
#     _input = input("Do you want to continue Loop ? (y/n): ")
    
#     if _input.lower() == 'n':
#         print("Exiting the loop.")
#         break
    
#     print("Continuing the loop...")

#       *continue Example user input*

# while True:
#     user_input = input("Enter a number (or 'q' to quit): ")

#     if user_input.lower() == 'q':
#         print("Exiting Loop ....")
#         break

#     if user_input.isdigit():
#         number = int(user_input)

#         if number % 2 == 0:
#             print("even number:", number)
#             continue  
#         else:
#             print("odd number:", number)
#     else:
#         print("Invalid input. Please enter a valid number or 'q' to quit.")

#        *while loop example User input*

# Names=[]
# new_name=""

# while new_name != "Quit":
#     new_name=input("Enter Name or Quit : ")
#     if new_name !="Quit":
#         Names.append(new_name)
# print("Exiting Loop")

#           *Pass Example user input*

# start = int(input("Enter any number"))
# End = int(input("Enter any number"))
# for i in range(start,End):
#     pass