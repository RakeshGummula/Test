def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2

print("Select  one operation to do : \n"\
      "1.Add \t         2.Subtract\n"\
      "3.Multiply \t 4.divide\n")

select =eval(input("select operation to perform 1/2/3/4 :"))
number1=eval(input("enter first number : "))
number2=eval(input("enter second number : "))

if select == 1:
    print(number1,"+",number2,"=",add(number1,number2))
elif select == 2:
    print(number1,"-",number2,"=",sub(number1,number2))
elif select == 3:
    print(number1,"*",number2,"=",multiply(number1,number2))
elif select == 4:
    print(number1,"/",number2,"=",divide(number1,number2))
else:
    print("Invalid Input ")