# Matching and Searching
# regex and searching functions
# regex re.match(), re.search() and re.findall()

# Match first word
import re
# match = re.searc(hr"\b\w+\b", text)

# print(match.group())

# Example 2: Validate email format or email address


# def validate_email(email):
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     if re.match(pattern, email):
#         return True
#     else:
#         return False


# # Example Usage
# email1 = "landrian345@gmail.com"
# email2 = "landrian345@gmailcom"

# print(validate_email(email2))
# print(validate_email(email1))

# Generators and Iterators
# 'yield' generator
# Iterator '__iter__' "__next__" iterator

def factorial(x):
    if x == 0:
        yield 1
    else:
        factor = 1
        for i in range(1, x+1):
            factor *= 1
        yield factor


    # Print the factorial of numbers 1 to 10
for i in range(1, 10):
    print(factorial(i))

# Example 3: Generate function that


def squares():
    for i in range(1, 10):
        yield i**2
# Create iterator object that yields the square of numbers from 1 -10


squares_iterator = squares()

# Print the first 5 square numbers from 1 to 10
for i in range(5):
    print(next(squares_iterator))

# Decorators
# Allows modification of the behavior of functions or
# classes without directly changing the source code.
# Context managers
# Multithreading and multiprocessing.


def my_decorator(func):
    def inner():
        print("Its my decorator")
        func()
    return inner()


@my_decorator
def outer_decorator():
    print("My outer decorator")


outer_decorator()
