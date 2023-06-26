# Group blocks of code(Functions)

def afternoon():
    print("Good Afternoon")


# Calling a function
afternoon()

# Arguments and parameters.


# def afternoon(fname, lname):
#     print("Good Afternoon, " + fname + " " + lname)

#     print(f"Good Afternoon {fname} {lname}")


# afternoon("John", "Doe")

# Modules
# A file containing python definitions and statements
# A simple Calculator module

# Code tobe used in module.py file


# def add(x, y):
#     return x + y


# def subtract(x, y):
#     return x - y


# print("================================================================")

# # Input and output in python
# # input ('prompt')
# # Examples:

# name = input("Enter your name :")
# print("My name is" + name)

# age = int(input("Enter your age :"))
# new_yr = age + 1
# print("New Year is", new_yr)

# Multiple inputs in python
# s, r, w = map(int,input("Enter your values :").split())
# print(s+r+w)
# print("The values are :", end=" ")

# Capturing input from tuple
w = (1, 2, 3, 4, 5)
print(w)

E = list(w)
E.append(int(input("Enter a new value: ")))
w = tuple(E)
print("Updated Tuple")
print(w)

mylist = list(map(int, input("Enter list values: ").split()))
set = set(map(int, input("Set values: ").split()))

print(mylist)
print(set)
