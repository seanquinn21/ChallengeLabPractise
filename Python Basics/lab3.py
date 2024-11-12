# Lab 3 - Introduction to Python and Virtual Environments

# ------------------------------------------
# 1. Setting Up and Using Virtual Environments
# ------------------------------------------

# Command to create a virtual environment (run in terminal, not in Python):
# python3 -m venv <env_name>

# Activating the virtual environment:
# Windows: <env_name>\Scripts\activate
# macOS/Linux: source <env_name>/bin/activate

# Deactivating the virtual environment:
# deactivate

# Listing installed packages:
# pip list

# Freezing installed packages to a requirements file:
# pip freeze > requirements.txt

# Installing packages from a requirements file:
# pip install -r requirements.txt


# ------------------------------------------
# 2. Basic Python Syntax and Common Commands
# ------------------------------------------

# Printing Output
print("Hello, World!")  # Outputs text to the console

# Basic Variables and Data Types
age = 25          # Integer
height = 5.9      # Float
name = "Alice"    # String
is_student = True # Boolean

# String Formatting
print(f"Hello, {name}! You are {age} years old.")


# ------------------------------------------
# 3. User Input and Casting
# ------------------------------------------

# Getting User Input
name = input("Enter your name: ")  # Prompts the user to enter text
print(f"Hello, {name}!")           # Prints a greeting with the entered name

# Casting Types
num1 = int(input("Enter first number: "))  # Converts input to integer
num2 = float(input("Enter a decimal number: "))  # Converts input to float


# ------------------------------------------
# 4. Control Flow: Conditional Statements
# ------------------------------------------

age = 20
if age >= 18:
    print("You are an adult.")
elif age > 12:
    print("You are a teenager.")
else:
    print("You are a child.")


# ------------------------------------------
# 5. Loops
# ------------------------------------------

# For Loop
for i in range(5):
    print("Hello, World!")  # Prints "Hello, World!" five times

# Using Enumerate in Loops
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Fruit {index}: {fruit}")

# While Loop
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1


# ------------------------------------------
# 6. Time Module and Countdown Timer
# ------------------------------------------

import time

# Creating a Countdown Timer
countdown = 5
while countdown > 0:
    print(countdown)
    time.sleep(1)   # Pauses for 1 second
    countdown -= 1
print("Time's up!")


# ------------------------------------------
# 7. Functions
# ------------------------------------------

# Defining a Function
def greet(name):
    return f"Hello, {name}!"

# Calling a Function
print(greet("Alice"))  # Outputs: Hello, Alice!

# Using __main__ to Control Script Execution
if __name__ == "__main__":
    print("This script is running directly.")


# ------------------------------------------
# 8. Basic Calculator Using Functions
# ------------------------------------------

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"

# Simple calculator loop
while True:
    # Taking inputs
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    operator = input("Enter operator (+, -, *, /): ")
    
    # Printing result
    print("Result:", calculate(num1, num2, operator))
    
    # Exit condition
    if input("Type 'quit' to exit, or press Enter to continue: ") == 'quit':
        break
