#        *1.Write a python program to remove a given  character from string.*

# String = input("Enter A String : ")
# char_to_remove = input("Enter character to Remove : ")

# AfterRemovechar = ""

# for char in String:
#     if char != char_to_remove:
#         AfterRemovechar+=char

# print("Input Given String : ",String)
# print(f"String After Removing '{char_to_remove}':\n",AfterRemovechar)



#         *2.Write a program to check String is Palindrome or not.*

# String=input("Enter A string :")

# String=String.casefold()

# if String == String[::-1]:
#     print("The String is Palindrome")
# else:
#     print("The String isn't Palindrome")

#       *3.Write a python program to check given character is vowel or consonant.*

# Characterinput=input("Enter a one Character :")
# c=Characterinput
# if (c == "A" or c =="a" or c=="E" or c=="e" or c=="I" or c=="i" or c=="o" or c=='O' or c=='u' or c=='U'):
#     print("Given Character is",c,"is a Vowel")
# else:
#     print('Given character is',c,'Is a Consonant')

#       *4.Write a python program to replace string space with given character in Python.*

# String_space=input('Enter a string with include spaces :')
# removespace= input("Enter replacing letter,symbol or Digit for Space :")
# String_space=String_space.replace(" ",removespace)
# print("String After Replacing Spaces:")
# print(String_space)


#       *5.Write a python program to count alphabets, digits, and special characters in the string.*
# countstring=input('Enter a String :')
# c = countstring
# alpahbets=digits=special=0

# for i in range(len(c)):
#     if (c[i].isalpha()):
#         alpahbets+=1
#     elif(c[i].isdigit()):
#         digits+=1
#     else:
#         special+=1

# print('Number of Alphabets in Given String : ',alpahbets)
# print("Number of Digits in given String : ",digits)
# print('''Number of Special Charcters in given String : ''',special)


#          *6.Write a python program to remove all the blank spaces in a given string.*
# Blankremove=input("Enter a String Include spaces :")
# Blankremove="".join(Blankremove.split())
# print(Blankremove)

# or
# Blankremove=input("Enter a String Include spaces :")
# Removeblank=Blankremove.replace(" ",'')
# print(Removeblank)


#           *7.Write a python program to find sum of integers in the string.*
# Sumofintegers=input("Enter A string with include  Numbers :")
# sums=0
# for i in Sumofintegers:
#     if (i.isnumeric()):
#         sums+=int(i)

# print("Sum of integers in given String is :",sums)


#           *8.Write a python program to Remove Repeated Character from String.*
removerepeat=input("Enter a String to remove duplicates :")
repeatremove=""
for char in removerepeat:
    if char not in repeatremove:
        repeatremove+=char
print(repeatremove)

