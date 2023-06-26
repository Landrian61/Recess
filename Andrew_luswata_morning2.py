# # Example 2
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def witdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             print("Insufficient Funds!")

#     def deposit(self, amount):
#         self.balance += amount

#     def display_balance(self):
#         print("Account Number:", self.account_number)
#         print("Balance:", self.balance)


# # Create Bank Account Object
# my_account = BankAccount("123456778", 1000)

# # Perform operations on bank account Object
# print(my_account.witdraw(20000))
# print(my_account.deposit(1000000))
# print(my_account.display_balance())

# # Example 2: University Student


# class Student:
#     def __init__(self, name, year, course):
#         self.name = name
#         self.year = year
#         self.course = course

#     def display_details(self):
#         print("Name : ", self.name)
#         print("Year :", self.year)
#         print("Course :", self.course)


# # Create Student Object
# my_student = Student("Andrew", 3, "Software Engineering")

# # Display Student details
# my_student.display_details()

# # Example 3


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# def greet(self):
#     print("Yoo, my name is ", self.name)
#     print("I am ", self.age, " years old!")


# # Create an object person
# person1 = Person("Andrew", 21)
# person2 = Person("Jemima", 24)

# print(person1.name)
# print(person1.age)
# print(person2.name)
# print(person2.age)

# # Invoke an object Metod
# person1.greet()
# person2.greet()

# # Exercise 1 Calculate te circumference of a circle
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius


# Exercise 2: Calculate te area and perimeter of a rectangle


# Calculate and display employee bonuses(15% of salary( employee1 :150000, employee2:230000)
# class Employee:
#     def __init__(self, name, salary):
#         self.salary = salary
#         self.name = name

#     def bonus(self):
#         return self.salary * 0.15

#     def display(self):
#         print("Name : ", self.name)
#         print("Salary :", self.salary)
#         print("Bonus :", self.bonus())


# # Create employee object
# employee1 = Employee("Andrew", 150000)
# employee2 = Employee("Jemima", 230000)

# # Display employee details
# employee1.display()
# employee2.display()

# Encapsulation
# Key goals of encapsulation are;
# 1. To protect objects from external changes
# 2. To protect objects from changes
# 3. Code organisation and Modularity.
# 4. To hide the implementation details of an object.

# Exaople with a bank account


# class BankAccount:
#     def __init__(self, account_number, balance):
#         # Encapsulates account number attrobute.
#         self.account_number = account_number
#         self.balance = balance  # Encapsulates balance attrobute

#         def deposit(self, amount):
#             self.balance += amount  # Encapsulates the deposit

#         def witdraw(self, amount):
#             if self.balance >= amount:
#                 self.balance -= amount
#             else:
#                 print("Insufficient Funds!")

#         def get_balance(self):
#             return self.balance


#    # Create Bank object
# my_account1 = BankAccount("123456778", 10000)

# # Access bank object modify encapsulated attributes indirectly.
# print(my_account1.get_balance())
# print(my_account1.account_number)
# my_account1.witdraw(5000)
# print(my_account1.get_balance())
# my_account1.deposit(10000)

# # Exercise 2: Convert 37 degrees celsius to fahrenheit.

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
        self.fahrenheit = (celsius * 9 / 5) + 32

    def display(self):
        print("Celsius :", self._celsius)
        print("Fahrenheit :", self.fahrenheit)


temp1 = Temperature(37)
temp1.display()
print("================================================")

# Assignment 2: Show encapsulation with employee information to give a
# pay incrementation (Salary with employee information to new salary) eg from 850000 to 1000000.


class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        self._salary = new_salary

    def increment_salary(self, increment_amount):
        self._salary += increment_amount


# Creating an employee object
employee = Employee("Kigoma Benjamin", 850000)

# Getting the current salary
current_salary = employee.get_salary()
print("Current Salary:", current_salary)

# Incrementing the salary by a given amount
increment_amount = 150000
employee.increment_salary(increment_amount)

# Getting the updated salary
updated_salary = employee.get_salary()
print("Updated Salary:", updated_salary)
