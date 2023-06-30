# Exceptions
# Exceptions are a way to handle errors or exceptional conditions that may occur during the execution of a program.
#  When an exceptional situation arises, an exception object is raised, and the normal flow of the program is interrupted.
#  If the exception is not handled, it will cause the program to terminate and display an error message.

def divide_numbers():
    try:
        a = int(input("Enter first number :"))
        b = int(input("Enter second number :"))
        result = a / b
        print(f"The result of division is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid operand types for division.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Division operation completed.")


# Example usage
divide_numbers()

# File handling
# File handling in Python is the process of working with files, which can be used to read data from or write data to files on a computer.
# 1. Opening a file:
#    To work with a file, you first need to open it using the open() function.
#    The open() function takes two parameters: the file name (or path) and the mode in which you want to open the file.
#    The mode can be "r" for reading, "w" for writing (overwriting existing file), "a" for appending (adding data to the end of an existing file),
#    or "x" for creating a new file.
# 2. Reading from a file:
#    Once a file is opened in read mode, you can read its contents using various methods.
#    The most common method is read(), which reads the entire file as a string.
#    You can also read the file line by line using the readline() method or get a list of all lines using the readlines() method.
# 3. Writing to a file:
#    When a file is opened in write or append mode, you can write data to it using the write() method.
#    If you open a file in write mode ("w"), it will overwrite the existing content.
#    To avoid overwriting, you can open the file in append mode ("a"), which allows you to add data to
#    the end of the file without removing the existing content.
# 4. Closing the file
#     After you finish working with a file, it's important to close it using the close() method.
#     This releases the system resources associated with the file.
#     However, a more recommended approach is to use the with statement, which automatically takes care of closing the file for you.
#     The with statement ensures that the file is properly closed, even if an exception occurs within the block.

# # Example usage
# # Opening a file in write mode and writing data to it
# file = open("example.txt", "w")
# file.write("Hello, World!\n")
# file.write("This is a demo file.\n")
# file.close()

# # Opening the same file in read mode and reading its contents
# file = open("example.txt", "r")
# content = file.read()
# print("File Contents:\n", content)
# file.close()

# # Opening the same file in read mode and reading line by line
# file = open("example.txt", "r")
# line = file.readline()
# print("First line:", line)
# lines = file.readlines()
# print("Remaining lines:", lines)
# file.close()

# # Opening the same file in append mode and appending more data to it
# file = open("example.txt", "a")
# file.write("Appending new line.\n")
# file.close()

# # Opening the same file in read mode again and printing its updated contents
# file = open("example.txt", "r")
# content = file.read()
# print("Updated File Contents:\n", content)
# file.close()

# # Using the with statement to automatically close the file
# with open("example.txt", "r") as file:
#     content = file.read()
#     print("File Contents using with statement:\n", content)
