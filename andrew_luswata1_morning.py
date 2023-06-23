"""# Membership operators
# Identity operators
# Arithmetic operators

# Addition
x = 33+77
print(x)
# Subtraction
x = 33-77
print(x)
# Multiplication
x = 33*77
print(x)
# Division
x = 33/77
print(x)
# Floor division
x = 33//77
print(x)
# Exponentiation
x = 33**2
print(x)
# Modulo
x = 33 % 77
print(x)

# Comparison operators
# Greater than
if x > 20:
    print("x is greater than 20")
    print(x > 20)

# Less than
if x < 20:
    print("x is less than 20")
    print(x < 20)

# Greater than or equal to
if x >= 20:
    print("x is greater than or equal to 20")
    print(x >= 20)

# Less than or equal to
if x <= 20:
    print("x is less than or equal to 20")
    print(x <= 20)

# Equal to
if x == 20:
    print("x is equal to 20")
    print(x == 20)

# Logical operators
# Logical AND operator
a = True
b = False

if a and b:
    print("a and b is True")
    print(a and b)

# Logical OR operator
a = True
b = False

if a or b:
    print("a or b is True")
    print(a or b)
    print(not a)
    print(not b)
# Assignment operators
a = 20
# Add and assign
a += 10
print(a)
# Subtract and assign
b = 25
b -= 5
print(b)
# Multiply and assign
c = 10
c *= 2
print(c)
# Divide and assign
d = 50
d /= 2
print(d)
# Modulo and assign
e = 5
e %= 2
print(e)
# Exponentiation and assign
f = 5
f **= 2
print(f)

# Membership assignment operators
colleges = ['COCIS', 'CEDAT', 'COBAMS', 'CONAS']
if 'COCIS' in colleges:
    print("COCIS" in colleges)
    print("COCIS" not in colleges)
    print("CEDAT" in colleges)
    print("COBAMS" not in colleges)
    print("CONAS" in colleges)

# Identity operators
# is operator
a = 20
b = 20
if a is b:
    print("a is b")
    print(a is b)
    print(a is not b)
# is not operator
a = 20
b = 20
c = [1, 2, 3]
d = [1, 2, 3]
if a is not b:
    print("a is not b")
    print(a is not b)
    print(a is b)
    print(c is d)
    print(c is not d)

# Bitwise operators
#Used to perform bitwise operations on individual bits in a binary number.
#Bitwise AND('&'): Perform bitwise AND operation between corresponding bits of two integers.
#Bitwise OR(''): Perform bitwise OR operation between corresponding bits of two integers.
#Bitwise XOR('^'): Perform bitwise XOR operations
#Bitwise NOT('~'): Perform bitwise NOT operations
#Bitwise Left shift('<<'): Perform bitwise left shift operations.
#Bitwise Right shift('>>'): Perform bitwise right shift operations.

# Bitwise AND
a = 33
b = 77
print(a & b)

# Bitwise OR
a = 33
b = 77
print(a | b)

# Bitwise XOR
a = 33
b = 77
print(a ^ b)

# Bitwise NOT
a = 33
print(~a)

# Bitwise Left shift
a = 33
print(a << 2)

# Bitwise Right shift
a = 33
print(a >> 2)"""

# Create a simple calculator function to calculate (add, subtract, multiply, divide)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    return x / y


def multiply(x, y):
    return x * y


def main():
    print('Welcome to my calculator.')
    number1 = float(input("Enter your first number  :"))
    number2 = float(input("Enter your second number  :"))
    operator = input("Enter your operator (+, -, *, /)  :")
    if operator == '+':
        result = add(number1, number2)

        print("The result is: ", result)
    elif operator == '-':
        result = subtract(number1, number2)
        print("The result is: ", result)
    elif operator == '*':
        result = multiply(number1, number2)
        print("The result is: ", result)
    elif operator == '/':
        result = divide(number1, number2)
        print("The result is: ", result)
    else:
        print("Invalid operator")


if __name__ == '__main__':
    main()

    # Assignment.tkinter
    # Create a calculator program with a GUI interface with your name eg 'luswata andrew's simple calculator program'
