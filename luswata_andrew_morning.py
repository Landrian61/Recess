# Control flow
age = 10
if (age < 18):
    print("You can not vote")

elif (age >= 18 and age <= 30):
    print("You are eligible to vote")
else:
    print("You can vote.")

# Loops
# For loop
cars = ['Tesla', 'Mercedes', 'BMW', 'Jeeps', 'Audi']
for car in cars:
    print(car)

# while loop
fruit = ['Apple', 'Mango', 'Pineapple', 'Kiwi']
count = 0
while (count < len(fruit)):
    print(fruit[count])
    count += 1

# Break and Continue statements
for n in range(1, 20):
    if n == 10:
        break
    if n % 2 == 0:
        continue
    print(n)
# Exceptions
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    z = x / y
    print(z)
except ZeroDivisionError:
    print("attempted to divide number by zero!")
finally:
    print("This is always executed")

# dictionary
# EXERCISE_DICTIONARY
emotions = {
    'sad': "I am sorry to hear that you are sad 😔",
    'angry': "Calmdown, you will be fine 😡",
    'disgust': "Why are you disgusted 🤮",
    'jolly': "I am very jolly 😄",
    'happy': "I am very happy 🤩",
    'surprised': "I am very surprised 😮",
    'fearful': "I am very fearful 😱"
}
user_emotions = input("How are you doing today?")
if user_emotions in emotions:
    print(emotions[user_emotions])
else:
    print("I don't understand your emotions. ")

# EXERCISE TWO
# Write a program to ask students about their mental health.
mental_status = {
    1: "You need mental attention",
    2: "Your mental health is alarming ",
    3: "You are worried",
    4: "You are anxious",
    5: "You are stressed",
    6: "You are depressed",
    7: "You are sad",
    8: "You are angry",
    9: "You are okay ",
    10: "You are 100% Sane",
}
mental = input(
    "What do you think is your mental health from a scale of 1 to 10? ")
try:
    mental = int(mental)
    if (mental in mental_status):
        print(mental_status[mental])
    else:
        print("Invalid input. Please enter a number between 1 and 10.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
