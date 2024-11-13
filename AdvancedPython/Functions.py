#------------------------------------------------#
#   1. Defining and Calling Functions
#------------------------------------------------#
# Functions in Python are defined using the `def` keyword, followed by the function name and parentheses `()`.
# Code inside the function is indented. To call a function, simply use its name followed by parentheses.

def greet():
    print("Hello, welcome to Python functions!")

# Calling the function
greet()


#------------------------------------------------#
#   2. Functions with Parameters
#------------------------------------------------#
# Parameters are variables listed inside the parentheses in the function definition.
# Arguments are the values passed to the function when calling it.
# Python functions can take any number of parameters.

def greet_user(name):
    print(f"Hello, {name}!")

# Calling the function with an argument
greet_user("Alice")


#------------------------------------------------#
#   3. Returning Values from Functions
#------------------------------------------------#
# Functions can return values using the `return` keyword.
# This allows functions to send back a result to the caller, which can be stored in a variable or used directly.

def add(a, b):
    return a + b

# Capture the return value in a variable
result = add(5, 10)
print("The sum is:", result)


#------------------------------------------------#
#   4. Default Parameter Values
#------------------------------------------------#
# You can assign default values to function parameters by using `parameter=value` in the function definition.
# If an argument for that parameter is provided, it overrides the default value.

def greet_user(name="User"):
    print(f"Hello, {name}!")

# Calling the function with and without an argument
greet_user("Alice")  # Output: Hello, Alice!
greet_user()         # Output: Hello, User!


#------------------------------------------------#
#   5. Using `*args` for Variable-Length Arguments
#------------------------------------------------#
# The `*args` syntax allows a function to accept any number of positional arguments.
# `*args` collects additional arguments as a tuple.

def print_numbers(*args):
    for number in args:
        print(number)

# Calling the function with multiple arguments
print_numbers(1, 2, 3, 4, 5)


#------------------------------------------------#
#   6. Using `**kwargs` for Variable-Length Keyword Arguments
#------------------------------------------------#
# The `**kwargs` syntax allows a function to accept any number of keyword arguments.
# `**kwargs` collects additional keyword arguments as a dictionary.

def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with keyword arguments
print_user_info(name="Alice", age=30, location="New York")


#------------------------------------------------#
#   7. Lambda Functions
#------------------------------------------------#
# Lambda functions are small, anonymous functions defined with the `lambda` keyword.
# They are often used for short, simple operations and take any number of arguments but only have one expression.

square = lambda x: x * x
print("Square of 5 is:", square(5))  # Output: Square of 5 is: 25

# Lambda functions are often used with functions like `map`, `filter`, and `sorted`.
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared numbers:", squared_numbers)  # Output: Squared numbers: [1, 4, 9, 16]


#------------------------------------------------#
#   8. Recursive Functions
#------------------------------------------------#
# Recursive functions are functions that call themselves. They need a base case to stop the recursion.
# Recursive functions are commonly used for problems that can be broken down into smaller, similar problems.

def factorial(n):
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive call

print("Factorial of 5 is:", factorial(5))  # Output: Factorial of 5 is: 120


#------------------------------------------------#
#   9. Function Scope and Global Variables
#------------------------------------------------#
# Variables created inside a function are local and cannot be accessed outside.
# If you need to modify a global variable within a function, use the `global` keyword.

x = 10  # Global variable

def modify_global():
    global x  # Declare x as global
    x = 20

modify_global()
print("Value of x after modification:", x)  # Output: Value of x after modification: 20


#------------------------------------------------#
#   10. Nested Functions and Closures
#------------------------------------------------#
# Functions can be defined inside other functions. Inner functions have access to variables in the outer function.
# Closures occur when an inner function remembers the state of its outer function even after the outer function finishes.

def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

# Calling the outer function and storing the inner function
closure = outer_function("Hello from the closure!")
closure()  # Output: Hello from the closure!


#------------------------------------------------#
#   11. Decorators
#------------------------------------------------#
# Decorators are functions that modify the behavior of another function.
# They are often used for logging, validation, or measuring performance.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.


#------------------------------------------------#
#   12. Passing Functions as Arguments
#------------------------------------------------#
# In Python, functions are first-class objects, meaning they can be passed as arguments to other functions.

def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x * 2, 5)
print("Result:", result)  # Output: Result: 10


#------------------------------------------------#
#   13. Docstrings
#------------------------------------------------#
# Docstrings are used to document what a function does. They are written as the first statement in a function.
# Docstrings can be accessed using `help()` or `function_name.__doc__`.

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

# Accessing the docstring
print(add.__doc__)  # Output: Returns the sum of two numbers.


#------------------------------------------------#
#   14. Type Hints (Python 3.5+)
#------------------------------------------------#
# Type hints specify the expected types of parameters and return values.
# Type hints do not enforce types but serve as documentation for better readability and can be checked with static analysis tools.

def multiply(a: int, b: int) -> int:
    return a * b

result = multiply(3, 4)
print("Multiplication result:", result)  # Output: Multiplication result: 12


#------------------------------------------------#
#   Summary of Key Points
#------------------------------------------------#
# - **Defining Functions**: Use `def function_name(parameters):` and call with `function_name()`.
# - **Parameters and Arguments**: Define functions with parameters, use default values, `*args` for variable-length arguments, and `**kwargs` for keyword arguments.
# - **Returning Values**: Use `return` to send results back to the caller.
# - **Lambda Functions**: Use `lambda` for small anonymous functions.
# - **Recursive Functions**: A function that calls itself; always define a base case.
# - **Global Variables**: Use `global` to modify global variables inside functions.
# - **Closures and Nested Functions**: Define a function inside another; inner functions can remember the outer function's state.
# - **Decorators**: Use to modify function behavior without changing its code.
# - **Docstrings and Type Hints**: Use docstrings for documentation and type hints for clarity.

# With these concepts, you’ll be able to create versatile, reusable, and well-documented functions in Python!
