#------------------------------------------------#
#   1. Defining a Basic Class
#------------------------------------------------#
# In Python, classes are defined using the `class` keyword followed by the class name.
# By convention, class names use CamelCase (e.g., `Person` or `BankAccount`).
# A class groups related data and functions together, creating a blueprint for objects.

class Person:
    pass  # `pass` is a placeholder indicating this class is currently empty

# This defines an empty class called `Person`. The `pass` statement does nothing but allows the class to be defined.
# A class with `pass` is typically a starting point for adding attributes and methods later.


#------------------------------------------------#
#   2. Creating an Instance of a Class (Object)
#------------------------------------------------#
# A class is just a blueprint until it is instantiated, meaning an object is created from it.
# To create an instance, call the class name with parentheses, like calling a function.

person1 = Person()  # Creates an instance (object) of the Person class
print(type(person1))  # Output: <class '__main__.Person'>

# `person1` is an object of the `Person` class. Each time you instantiate, a new object is created.


#------------------------------------------------#
#   3. Adding an `__init__` Method (Constructor)
#------------------------------------------------#
# The `__init__` method is a special method in Python called a "constructor."
# It runs automatically whenever a new instance of the class is created.
# The `self` parameter in `__init__` refers to the instance being created.

class Person:
    def __init__(self, name, age):
        self.name = name  # Creates an instance attribute `name`
        self.age = age    # Creates an instance attribute `age`

# The `__init__` method allows us to set initial values for attributes when creating an object.

# Creating an instance with attributes
person2 = Person("Alice", 30)
print(person2.name)  # Output: Alice
print(person2.age)   # Output: 30

# Explanation:
# - `self.name = name` and `self.age = age` assign values to instance attributes.
# - `self` is a reference to the instance itself, which is why each object has its own `name` and `age` values.


#------------------------------------------------#
#   4. Instance Attributes vs. Class Attributes
#------------------------------------------------#
# Instance attributes are unique to each instance and defined within `__init__`.
# Class attributes are shared across all instances of the class and are defined outside `__init__`.

class Person:
    species = "Homo sapiens"  # Class attribute

    def __init__(self, name, age):
        self.name = name      # Instance attribute
        self.age = age        # Instance attribute

# Creating instances
person3 = Person("Bob", 25)
person4 = Person("Eve", 28)

# Accessing instance and class attributes
print(person3.name)     # Output: Bob (instance attribute)
print(person4.species)  # Output: Homo sapiens (class attribute)

# Explanation:
# - `species` is a class attribute and shared by all instances.
# - `name` and `age` are instance attributes, unique to each `Person` instance.


#------------------------------------------------#
#   5. Defining Methods (Functions within a Class)
#------------------------------------------------#
# Methods are functions defined within a class that operate on the instance (object).
# Methods always take `self` as the first parameter, which represents the instance.

class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):  # A method that belongs to the `Person` class
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an instance and calling a method
person5 = Person("Charlie", 35)
person5.greet()  # Output: Hello, my name is Charlie and I am 35 years old.

# Explanation:
# - The `greet` method uses `self.name` and `self.age` to access instance attributes.


#------------------------------------------------#
#   6. The `self` Parameter
#------------------------------------------------#
# The `self` parameter in methods refers to the instance on which the method is called.
# It allows methods to access attributes and other methods within the same object.
# Every instance method in Python must have `self` as its first parameter.

class Person:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f"My name is {self.name}")

person6 = Person("Diana")
person6.say_name()  # Output: My name is Diana

# Explanation:
# - `self.name` inside `say_name` refers to the `name` attribute of the `person6` instance.
# - `self` is automatically passed to `say_name` when you call `person6.say_name()`.


#------------------------------------------------#
#   7. Modifying Attributes within Methods
#------------------------------------------------#
# Methods can modify attributes by directly accessing them with `self.attribute_name`.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def have_birthday(self):
        self.age += 1  # Increase the age attribute by 1
        print(f"Happy birthday, {self.name}! You are now {self.age}.")

person7 = Person("Emily", 29)
person7.have_birthday()  # Output: Happy birthday, Emily! You are now 30.

# Explanation:
# - `self.age += 1` modifies the instance attribute `age` directly.


#------------------------------------------------#
#   8. Using `__str__` for String Representation
#------------------------------------------------#
# The `__str__` method provides a human-readable string representation of an object.
# When you print an object, Python automatically calls `__str__` to get a string representation.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

person8 = Person("Frank", 40)
print(person8)  # Output: Person(name=Frank, age=40)

# Explanation:
# - `__str__` allows you to define how an instance of `Person` should be printed.


#------------------------------------------------#
#   9. Encapsulation with Private Attributes (Conventional)
#------------------------------------------------#
# In Python, you can indicate that an attribute or method is intended to be private by prefixing it with `_` or `__`.
# This is a convention, as Python does not strictly enforce private attributes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Single underscore suggests "internal use"
        self.__secret = "I love coding"  # Double underscore makes it harder to access directly

    def reveal_secret(self):
        print(self.__secret)

person9 = Person("George", 50)
person9.reveal_secret()  # Output: I love coding

# Attempting to access `__secret` directly will fail due to name mangling:
# print(person9.__secret)  # Raises AttributeError

# Explanation:
# - `_age` is a convention to signal "private" use; `__secret` is name-mangled for extra protection.


#------------------------------------------------#
#   10. Summary of Key Points for Basic Classes
#------------------------------------------------#
# - **Class Definition**: Use `class ClassName:` to define a class.
# - **Constructor (`__init__`)**: Initialize attributes when creating an instance.
# - **Instance Attributes**: Defined within `__init__` using `self.attribute = value`.
# - **Class Attributes**: Shared across all instances, defined outside `__init__`.
# - **Methods**: Define functions within a class to operate on instances, using `self` to refer to the instance.
# - **`self` Parameter**: Refers to the instance calling the method.
# - **Private Attributes**: Prefix attributes with `_` or `__` to indicate restricted access.
# - **`__str__` Method**: Provides a string representation for the class.

# With these basics, you can define, instantiate, and work with Python classes effectively!
