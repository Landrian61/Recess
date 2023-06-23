# Individual Assignment
# Exercise1 (Lists)

# 1. Create a list with 5 items (names of people) and write a python program to output the 2nd item.
names = ['John', 'Jennifer', 'Jenna', 'Brian','Louis']
print(names[1])
print('\n================================================================================================')

# 2. Write a python program to change the value of the first item to a new value
names[0]='Mellow'
print('\n================================================================================================')

# 3. Write a python program to add a sixth item to the list
names.append('Sarah')
print(names)
print('\n================================================================================================')

# 4. Write a python program to add “Bathel” as the 3rd item in your list
names.insert(2,'Bathel')
print(names)
print('\n================================================================================================')

# 5. Write a python program to remove the 4th item from the list
names.pop(2)
print(names)
print('\n================================================================================================')

# 6. Use negative indexing to print the last item in your list
print(names[-1])
print('\n================================================================================================')

# 7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
names1 = ['John', 'Jennifer', 'Jenna', 'Brian','Louis','Mary','Sally']
print(names1[3:5])
print('\n================================================================================================')

# 8. Write a list of countries and make a copy of it.
countries = ['India', 'USA', 'China', 'Japan', 'Germany', 'France', 'Italy']
countries1 = countries.copy()
print(countries1)
print('\n================================================================================================')

# 9. Write a python program to loop through the list of countries
for country in countries:
    print(country)
    print('\n================================================================================================')

# 10. Write a list of animal names and sort them in both descending and ascending order.
animals = ['cat', 'dog', 'monkey', 'parrot', 'tiger']
animals.sort()
print(animals)
animals.sort(reverse=True)
print(animals)
print('\n================================================================================================')

# 11. Using the list above, write a python program to output only animal names with the letter ‘a’ in them
for animal in animals:
    if 'a' in animal:
        print(animal)
print('\n================================================================================================')         

# 12. Write two lists, one containing your first names and the other your second names. Join the two lists.
fname = ['John', 'Jennifer', 'Jenna', 'Brian','Louis']
lname = ['Mary', 'Sarah', 'Bathel']
fullname = fname + lname
print(fullname)
print('\n================================================================================================')

# 13. Write a python program to print the length of the list
print(len(fullname))
print('\n================================================================================================')

# Exercise2 (Tuples)

""" 1. Consider the tuple below;
 x = (“samsung”, “iphone”, “tecno”, “redmi”)
Write a python program to output your favorite phone brand"""
x = ('samsung', 'iphone', 'tecno', 'redmi')
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print('\n================================================================================================')

# 2. Use negative indexing to print the 2nd last item in your tuple.
print(x[-1])
print('\n================================================================================================')

# 3. Using the phones list above, write a python program to update “iphone” to “itel”
list_x = list(x)
list_x[1]= 'itel'
x = (list_x)
print(x)
print('\n================================================================================================')

# 4. Write a python program to add “Huawei” to your tuple.
x.append('Huawei')
print(x)
print('\n================================================================================================')

# 5. Write a python program to loop through the tuple above.
for phone in x:
    print(phone)
print('\n================================================================================================')    

# 6. Write a python program to remove/delete the first item in your tuple.
x.pop(0)
print(x)
print('\n================================================================================================')

# 7. Using the tuple() constructor, create a tuple of the cities in Uganda.
cities = tuple(['Kampala', 'Entebbe', 'Jinja', 'Gulu', 'Mbarara'])
print(cities)
print('\n================================================================================================')

# 8. Write a python program to unpack your tuple.
a, b, c, d , e= cities
print(a, b, c, d)
print('\n================================================================================================')

# 9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
for city in cities[3:5]:
    print(city)
print('\n================================================================================================')    

# 10. Write two tuples, one containing your first names and the other your second names. Join the two tuples.
fname = ('John', 'Jennifer', 'Jenna', 'Brian','Louis')
lname = ('Mary', 'Sarah', 'Bathel')
fullname = fname + lname
print(fullname)
print('\n================================================================================================')

# 11. Write a python program to print the length of the tuple
print(len(fullname))
print('\n================================================================================================')

# 11. Create a tuple of colors and multiply it by 3.
colors = ('red', 'green', 'blue', 'yellow')
print(colors * 3)
print('\n================================================================================================')

# 12. Return the number of times 8 appears in this tuple thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(8))
print('\n================================================================================================')

# Exercise3 (Sets)

# 1. Use the set() constructor to create a set of 3 of your favorite beverages.
beverages = set(['tea', 'coffee', 'milk'])
print(beverages)
print('\n================================================================================================')

# 2. Use the correct method to add 2 more items to the beverages set.
beverages.add('water')
beverages.add('juice')
print(beverages)
print('\n================================================================================================')

# 3. Use the correct method to remove the item “milk” from the beverages set.
beverages.remove('milk')
print(beverages)
print('\n================================================================================================')

# 3. Given the set below;
# mySet = {“oven”, “kettle”, “microwave”, “refrigerator”}
# Check if microwave is present in the set.
mySet = {'oven', 'kettle', 'microwave', 'refrigerator'}
print(mySet.__contains__('microwave'))
print('\n================================================================================================')

# 4. Write a python program to remove “kettle” from the set above.
mySet = {'oven', 'kettle', 'microwave', 'refrigerator'}
mySet.remove('kettle')
print(mySet)
print('\n================================================================================================')

# 5. Write a python program to loop through the set above.
mySet = {'oven', 'kettle', 'microwave', 'refrigerator'}
for item in mySet:
    print(item)
print('\n================================================================================================')

# 6. Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.
mySet = {'oven', 'kettle', 'microwave', 'refrigerator'}
myList = ['blender', 'boiler']
mySet.update(myList)
print(mySet)
print('\n================================================================================================')

# 7. Write two sets, one containing your ages and the other your first names. Join the two sets.
ages = {10,20,30,40,50}
fname = {'John', 'Jennifer', 'Jenna', 'Brian','Louis'}
fullname = fname.union(ages)
print(fullname)
print('\n================================================================================================')

# Exercise4 (Strings)
# 1. Declare two variables, an integer and a string and use the correct method to concatenate the two variables
age = 10
name = 'John'
print(str(age) + name)
print('\n================================================================================================')

# 2. Consider the example below;
# txt = “ Hello, Uganda! ”
# Output the string without spaces at the beginning, in the middle and at the end.
txt = " Hello, Uganda! "
print(txt.strip())
print('\n================================================================================================')

# 3. Write a python program to convert the value of ‘txt’ to uppercase.
txt = " Hello, Uganda! "
print(txt.upper())
print('\n================================================================================================')

# 4. Write a python program to replace character ‘U’ with ‘V’ in the string above.
txt = " Hello, Uganda! "
print(txt.replace('U', 'V'))
print('\n================================================================================================')

# 5. Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position.
# y = “I am proudly Ugandan”
y = "I am proudly Ugandan"
print(y[3:5])
print('\n================================================================================================')

# 6. The piece of code below will give an error when output;
# x = “All “Data Scientists” are cool!”
# Write a python program to correct it.
x = "All “Data Scientists” are cool!"
print(x.replace("Data Scientists", "Data Scientists"))
print('\n================================================================================================')

# Exercise5 (Dictionaries)
# 1. With reference to the dictionary below, write a python program to print the value of the shoe size.
# Add this dictionary to your .py file
# Shoes = {
# “brand” : “Nick”,
# “color” : “black”,
# “size” : 40 }
Shoes = {
    'brand': "Nike",
    'color': "black",
    'size': 40
 }
print(Shoes['size'])

# 2. Write a python program to change the value “Nick” to “Adidas”
Shoes['brand'] = 'Adidas'
print(Shoes['brand'])

# 3. Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
Shoes['type'] = "sneakers"
print(Shoes['type'])

# 4. Write a python program to return a list of all the keys in the dictionary above.
print(Shoes.keys())
print('\n================================================================================================')

# 5. Write a python program to return a list of all the values in the dictionary above.
print(Shoes.values())
print('\n================================================================================================')

# 6. Check if the key “size” exists in the dictionary above.
print(Shoes.__contains__('size'))
print('\n================================================================================================')

# 7. Write a python program to loop through the dictionary above.
for key, value in Shoes.items():
    print(key, value)

# 8. Write a python program to remove “color” from the dictionary.
Shoes.pop('color')
print(Shoes)
print('\n================================================================================================')

# 9. Write a python program to empty the dictionary above.
Shoes.clear()
print(Shoes)
print('\n================================================================================================')

# 10. Write a dictionary of your choice and make a copy of it.
person = {
    'Name': "Andrew",
    'Gender': "male",
    'age': 40
 }
person2 = person.copy()
print(person2)
print('\n================================================================================================')

# 11. Write a python program to show nested dictionaries
fruits = {
    'berry' :{
        'name': "strawberry",
        'color': "red"
    },
    'drupe' :{
        'name': "apple",
        'color': "red"
    },
    'succulent':{
        'name': "mango",
        'color': "yellow"
    }
}
print(fruits)
for fruit in fruits:
    print(fruits[fruit])
