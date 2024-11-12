#------------------------------------------------#
#   1. Basic Syntax and Data Types
#------------------------------------------------#
# Write a function that takes a string as input and returns the string with each word capitalized.
# This question tests your understanding of string manipulation and functions.

def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())

# Example usage
print(capitalize_words("hello world"))  # Output: "Hello World"


#------------------------------------------------#
#   2. Control Flow and Conditionals
#------------------------------------------------#
# Write a function that takes an integer as input and returns "Even" if the number is even and "Odd" if the number is odd.
# This question tests your ability to use conditionals and basic arithmetic operators.

def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# Example usage
print(even_or_odd(5))  # Output: "Odd"
print(even_or_odd(8))  # Output: "Even"


#------------------------------------------------#
#   3. Loops and Iteration
#------------------------------------------------#
# Write a function that returns the sum of all even numbers from 1 to 100.
# This question tests your ability to use loops, list comprehension, and conditionals.

def sum_of_evens():
    return sum(num for num in range(1, 101) if num % 2 == 0)

# Example usage
print(sum_of_evens())  # Output: 2550


#------------------------------------------------#
#   4. Functions and Recursion
#------------------------------------------------#
# Write a recursive function that calculates the factorial of a given integer.
# This question tests your understanding of functions, recursion, and base/recursive cases.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120


#------------------------------------------------#
#   5. List and Dictionary Comprehensions
#------------------------------------------------#
# Write a function that takes a list of integers and returns a dictionary with each integer as a key and its square as the value.
# This question tests your knowledge of dictionary comprehension and basic iteration.

def squares_dict(numbers):
    return {num: num ** 2 for num in numbers}

# Example usage
print(squares_dict([1, 2, 3]))  # Output: {1: 1, 2: 4, 3: 9}


#------------------------------------------------#
#   6. Removing Duplicates from a List
#------------------------------------------------#
# Write a function that removes duplicate values from a list without changing the order of elements.
# This question tests your knowledge of list operations and set-based duplicate removal.

def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# Example usage
print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # Output: [1, 2, 3, 4]


#------------------------------------------------#
#   7. Object-Oriented Programming (OOP)
#------------------------------------------------#
# Define a `BankAccount` class with methods to deposit, withdraw, and check the balance.
# This question tests your understanding of class structures, methods, and instance variables.

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.balance

# Example usage
account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # Output: 150


#------------------------------------------------#
#   8. File Handling
#------------------------------------------------#
# Write a function that reads a file and counts the occurrences of each word.
# This question tests your ability to handle file I/O, string manipulation, and dictionaries.

def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Usage: Save this code to run it on an existing file with sample text.


#------------------------------------------------#
#   9. Exception Handling
#------------------------------------------------#
# Write a function that takes two numbers and divides the first by the second.
# Use exception handling to manage cases of division by zero.
# This question tests your understanding of error handling with try-except blocks.

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

# Example usage
print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: "Cannot divide by zero"


#------------------------------------------------#
#   10. Working with External Libraries (Pandas)
#------------------------------------------------#
# Use Pandas to read a CSV file and return the sum of values in a specified column.
# This question tests your ability to use external libraries, specifically Pandas for data manipulation.

import pandas as pd

def column_sum(file_path, column_name):
    df = pd.read_csv(file_path)
    return df[column_name].sum()

# Example usage: 
# Run this code by specifying a file_path to a valid CSV file and a column name.


#------------------------------------------------#
#   11. Algorithm Implementation
#------------------------------------------------#
# Write a function that checks if a string is a palindrome (reads the same forwards and backwards).
# This question tests your understanding of string slicing and logical conditions.

def is_palindrome(s):
    return s == s[::-1]

# Example usage
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False


#------------------------------------------------#
#   12. Regular Expressions
#------------------------------------------------#
# Write a function that validates if a given email address has a valid format.
# This question tests your understanding of pattern matching with regular expressions.

import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

# Example usage
print(is_valid_email("test@example.com"))  # Output: True
print(is_valid_email("invalid-email"))     # Output: False


#------------------------------------------------#
#   13. Functional Programming with Map and Lambda
#------------------------------------------------#
# Use `map` to square each element in a list using a lambda function.
# This question tests your understanding of functional programming with map and lambda.

def square_numbers(numbers):
    return list(map(lambda x: x ** 2, numbers))

# Example usage
print(square_numbers([1, 2, 3]))  # Output: [1, 4, 9]


#------------------------------------------------#
#   14. Data Serialization with JSON
#------------------------------------------------#
# Write a function that reads data from a JSON file and returns it as a Python dictionary.
# This question tests your understanding of JSON handling and file I/O.

import json

def read_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

# Usage: Save this code to run it on a JSON file.


#------------------------------------------------#
#   15. Unit Testing with the Unittest Library
#------------------------------------------------#
# Write unit tests for a function that calculates the factorial of a number.
# This question tests your ability to write tests using the `unittest` library.

import unittest

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(3), 6)

# Run tests
if __name__ == "__main__":
    unittest.main()
