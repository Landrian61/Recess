# Dictionaries in Python
# Stores data values in key-value pairs, ordered , changeable and dont allow duplicates.
phone = {
    'brand': 'Samsung',
    'model': 'Galaxy S23 Ultra',
    'price': 1499,
    'ram': '16GB',
    'storage': '512GB',
    'processor': 'Qualcomm Snapdragon 8 Gen 2',
}
print(phone)

print(len(phone))

print(phone.keys())

print(phone.items())

print(phone.get('brand'))

print(phone.get('model'))

print(type(phone))

print(type(phone.values()))

print(type(phone.keys()))

print(type(phone.items()))

# Exercise One: Use the values()method to return a list of all values in a dictionary
print(phone.values())

# Exercise Two: Check if a key exists in the dictionary

if "brand" in phone.keys():
    print("Key 'brand' exists in the dictionary.")
else:
    print("Key 'brand' does not exist in the dictionary.")


# Exercise Three:how to change dictionary items and update them
phone['brand'] = 'Apple'

print(phone)

# Exercise Four: how to add and remove dictionary items
phone['color'] = 'black'

print(phone)

del phone['color']

# Exercise Five: how to iterate through a dictionary and how to nest them
for key, value in phone.items():
    print(key, value)

# Create a nested dictionary
student = {
    "name": "John",
    "age": 20,
    "grades": {
        "math": 85,
        "science": 92,
        "history": 78
    }
}
# Accessing nested dictionary values
print(student["name"])
print(student["age"])
print(student["grades"]["math"])
print(student["grades"]["science"])
print(student["grades"]["history"])

# Integers, floats, Complex numbers
x = 20
y = 20.5
z = 5j

print(type(x))
print(type(y))
print(type(z))

# Integers.
values = (12, 288829183, -21)
for i in values:
    print(type(i))

# Conversion.
types = (10, 12.5, 10j)
for i in types:
    if (type(i) == int):
        a = complex(i)
        print(a)
    elif (type(i) == float):
        b = int(i)
        print(b)
    elif (type(i) == complex):
        print(i)

# Casting
a = int(20.5)
b = float(20.5)
c = complex(20.5)

print(a)
print(b)

# Strings
x = "Hello World"
y = 'Hello World'
print(x)
print(y)
print(type(x))
print(type(y))

# Multiline Strings
x = """Hello World
This is a multiline string
Want Some more!"""
print(x)
print(type(x))

# Strings as arrays
x = "Hello Andrew"

print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])

# Exercise1:Use len() function to determine the length of a string
print(len(x))

# Exercise 2: Example of using a for loop in a string
for i in x:
    print(i)

# Exercise 3: Example of slicing a string
print(x[0:3])
print(x[3:6])
print(x[3:])
print(x[:3])

# Modifying Strings
name = "Alice"
print(name.lower())
print(name.upper())

# Removing whitespaces from strings
x = "   Hello   Alice   !"
print(x.strip())

# String Concatenation
x = "Hello "
y = "Alice"
z = x + y
print(z)

# Concatenation of strings to numbers
x = "Hello "
y = 5
z = x + str(y)
print(z)

# Format string
x = "I am {} years old"
age = 10
print(x.format(age))

# Booleans
print(10 > 20)
print(10 < 20)

# Exercise: Use a condition to use booleans
is_raining = True
is_sunny = False

if is_raining:
    print("It is raining")
elif is_sunny:
    print("It's a sunny day.")
else:
    print("Neither raining nor sunny.")
