'''write a python program that allows you to add an employee with domain, name, empid, and email details 
using user input and then print the employee's details. '''
domain={}
name={}
empid={}
emailid={}

numberofemp=int(input("enter a number of employee wants to add : "))

for i in range(numberofemp):
    domain[i]=input(f"enter domain of employee {i+1}: ")
    name[i]=input(f"enter name of employee{i+1}: ")
    empid[i]=input(f"enter employee ID of employee {i+1}: ")
    emailid[i]=input(f"enter email id of employee {i+1}: ")

for i in range(numberofemp):
    print(f'\n employee {i+1} Details : ')
    print(f"Domain :{domain[i]}")
    print(f'Name :{name[i]}')
    print(f"Employee ID : {empid[i]}")
    print(f"Email ID : {emailid[i]}")