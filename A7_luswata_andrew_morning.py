# # Context Managers.
# """ Object that defines temporary context for a block of code
# Example1: Demonstrate a context manager to open a file and return a context manager instance.
# """

# import multiprocessing
# import threading
# import time


# def open_file(filename):
#     # open file and return a context manager instance
#     file = open(filename, 'r')

#     def __enter__():
#         return file

#     def __exit__(self, exc_type, exc_value, exc_tb):
#         file.close

#         return __enter__, __exit__


# with open_file('my_file.txt') as f:
#     contents = f.read()

# # Example2: Demnstrating a context manager using a time series


# class Timer:
#     def __enter__(self):
#         self.start = time.time()

#     def __exit__(self, exc_type, exc_value, traceback):
#         end_time = time.time()
#         execution_time = end_time - self.start
#         print(f"The time for this execution {execution_time} seconds elapsed")


# # Example Usage
# with Timer():
#     # Measure Execution Time
#     time.sleep(2)

# # Multithreading and Multiprocessing
# # Techniques that can be used to improve te performance of a python program
# # Multithreading: Technique where multiple threads are created within a single process
# # Multiprocessing: Technique where multiple threads are created.

# # Example of Multithreading


# def task(name):
#     print(f"Running task {name}")


# # Create Multiple threads
# threads = []
# for i in range(10):
#     t = threading.Thread(target=task, args=(f"Thread {i}",))
#     threads.append(t)
#     t.start()

# # Wati for all threads to finish

# for t in threads:
#     t.join()

# # Example 4: Multiprocessing demo


# def process(name):
#     print(f"Processing task {name}")


# # Create a pool of processes
# pool = multiprocessing.Pool(processes=5)

# # Submit multiple tasks to pool
# for i in range(6):
#     pool.apply_async(process, args=(f"Process {i}",))

# # Close te pool and wait for all processes to finish
# pool.close()
# pool.join()

# # Example 5: Demonstrating use of both multithreading and multiprocessing.


# def task(name):
#     print(
#         f"Running task {name} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name}")


# # Create multiple threads
# threads = []
# for i in range(4):
#     t = threading.Thread(target=task, args=(f"Thread {i}",))
#     threads.append(t)
#     t.start()

# # Wait for all threads to finish
# for i in threads:
#     t.join()

# Assignment.
################################################################
# 1a) Show a context manager for file handling that automatically opens and closes a file.
# class FileHandler:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None

#     def __enter__(self):
#         self.file = open(self.filename, self.mode)  # open the file
#         return self.file

#     def __exit__(self, exc_type, exc_value, traceback):
#         self.file.close()  # close the file


# Example Usage
# with FileHandler('example.txt', 'r') as file:
#     contents = file.read()
#     print(contents)

# b) Shows a context manager for managing a database connection.
# import sqlite3

# class DatabaseConnection:
#     def __init__(self, dbname):
#         self.dbname = dbname
#         self.conn = None

#     def __enter__(self):
#         self.conn = sqlite3.connect(self.dbname) # Opening connection to database
#         return self.conn

#     def __exit__(self, exc_type, exc_value, traceback):
#         self.conn.close() # Closing connection to database


# # Example Usage
# with DatabaseConnection('example.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users")
#     results = cursor.fetchall()
#     for row in results:
#         print(row)

# c) Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time.
import threading
import multiprocessing
import time


def worker_thread(seconds):
    print(f"Thread started: {threading.currentThread().name}")
    time.sleep(seconds)
    print(f"Thread finished: {threading.currentThread().name}")


def worker_process(seconds):
    print(f"Process started: {multiprocessing.current_process().name}")
    time.sleep(seconds)
    print(f"Process finished: {multiprocessing.current_process().name}")


# Multithreading example
threads = []
for i in range(1, 6):
    t = threading.Thread(target=worker_thread, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Multiprocessing example
processes = []
for i in range(1, 6):
    p = multiprocessing.Process(target=worker_process, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()
