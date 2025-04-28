"""
Module 6 Programming Assignment - Concurrency in Python

This script contains solutions for the programming problems related to:
- File handling (13.1, 13.2, 13.3)
- Multiprocessing (15.1)
"""

import multiprocessing
import random
import time
from datetime import datetime

def problem_13_1():
    """
    Problem 13.1: Write the current date as a string to the text file today.txt.
    """
    print("\n--- Problem 13.1 ---")
    
    # Get the current date as a string
    current_date = datetime.now().strftime("%Y-%m-%d")
    print(f"Current date: {current_date}")
    
    # Write the date to today.txt
    with open('today.txt', 'w') as file:
        file.write(current_date)
        
    print("Date written to today.txt")

def problem_13_2():
    """
    Problem 13.2: Read the text file today.txt into the string today_string.
    """
    print("\n--- Problem 13.2 ---")
    
    # Read the contents of today.txt into today_string
    with open('today.txt', 'r') as file:
        today_string = file.read()
        
    print(f"Contents of today.txt: {today_string}")
    
    return today_string

def problem_13_3(today_string):
    """
    Problem 13.3: Parse the date from today_string.
    """
    print("\n--- Problem 13.3 ---")
    
    # Parse the date from today_string
    parsed_date = datetime.strptime(today_string, "%Y-%m-%d")
    
    print(f"Parsed date: {parsed_date}")
    print(f"Year: {parsed_date.year}")
    print(f"Month: {parsed_date.month}")
    print(f"Day: {parsed_date.day}")

def worker_process():
    """
    Worker function for multiprocessing.
    Waits a random time between 0-1 seconds and prints the current time.
    """
    # Wait a random number of seconds between 0 and 1
    wait_time = random.random()
    time.sleep(wait_time)
    
    # Print the current time
    current_time = datetime.now().strftime("%H:%M:%S.%f")
    process_name = multiprocessing.current_process().name
    print(f"Process {process_name} - Current time: {current_time} (waited {wait_time:.4f} seconds)")

def problem_15_1():
    """
    Problem 15.1: Use multiprocessing to create three separate processes.
    Each process waits a random number of seconds between 0 and 1,
    prints the current time, and then exits.
    """
    print("\n--- Problem 15.1 ---")
    
    # Create three separate processes
    processes = []
    
    for i in range(3):
        process = multiprocessing.Process(target=worker_process, name=f"Worker-{i+1}")
        processes.append(process)
        process.start()
        print(f"Started process {process.name} with PID: {process.pid}")
    
    # Wait for all processes to complete
    for process in processes:
        process.join()
    
    print("All processes have completed.")

def main():
    """Main function to run all problems."""
    print("Module 6 Programming Assignment - Concurrency in Python")
    
    # Run Problem 13.1
    problem_13_1()
    
    # Run Problem 13.2
    today_string = problem_13_2()
    
    # Run Problem 13.3
    problem_13_3(today_string)
    
    # Run Problem 15.1
    problem_15_1()

if __name__ == "__main__":
    main()