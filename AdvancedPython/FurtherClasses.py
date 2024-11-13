#------------------------------------------------#
#   1. Class Inheritance
#------------------------------------------------#
# Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).
# The child class can extend or modify the functionality of the parent class.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

# Dog inherits from Animal
class Dog(Animal):
    def speak(self):  # Overrides the parent class's speak method
        return "Woof!"

# Creating an instance of Dog
dog = Dog("Buddy")
print(dog.name)      # Output: Buddy (inherited from Animal)
print(dog.speak())   # Output: Woof! (overridden method)

# Explanation:
# - `Dog` inherits from `Animal`, so it has the `name` attribute and can call `speak`.
# - The `speak` method in `Dog` overrides the one in `Animal`.


#------------------------------------------------#
#   2. The `super()` Function
#------------------------------------------------#
# `super()` is used to call a method from the parent class.
# This is especially useful in the `__init__` method to ensure proper initialization of inherited attributes.

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calls the parent class's __init__ method
        self.breed = breed

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)   # Output: Buddy (from Animal)
print(dog.breed)  # Output: Golden Retriever (from Dog)

# Explanation:
# - `super().__init__(name)` calls `Animal`’s `__init__` to set the `name` attribute.
# - `Dog` adds an additional attribute `breed`.


#------------------------------------------------#
#   3. Class Methods
#------------------------------------------------#
# Class methods are methods that operate on the class itself, rather than on an instance.
# They are defined using the `@classmethod` decorator, and the first parameter is `cls` (not `self`).

class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_species(cls):
        return cls.species

print(Dog.get_species())  # Output: Canine

# Explanation:
# - `get_species` is a class method that accesses the class attribute `species`.
# - `@classmethod` makes `get_species` available on the class itself (`Dog.get_species()`).


#------------------------------------------------#
#   4. Static Methods
#------------------------------------------------#
# Static methods are methods that do not operate on an instance or the class directly.
# They are defined using the `@staticmethod` decorator and do not take `self` or `cls` as parameters.

class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 10))  # Output: 15

# Explanation:
# - `add` is a static method that takes two parameters and returns their sum.
# - Static methods are like regular functions but are defined within a class for organizational purposes.


#------------------------------------------------#
#   5. Properties and Getters/Setters
#------------------------------------------------#
# Properties allow controlled access to instance attributes.
# Use the `@property` decorator to define a method as a getter, and `@attribute.setter` for a setter.

class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private attribute

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

# Creating an instance of Circle
circle = Circle(5)
print(circle.radius)     # Output: 5
circle.radius = 10       # Sets the radius to 10
# circle.radius = -5     # Raises ValueError

# Explanation:
# - `@property` makes `radius` accessible like an attribute.
# - `@radius.setter` controls how the attribute can be set, adding validation.


#------------------------------------------------#
#   6. Dunder (Magic) Methods and Operator Overloading
#------------------------------------------------#
# Dunder methods (also called magic methods) allow objects to interact with Python operators.
# For example, `__add__` allows overloading the `+` operator, and `__str__` provides a string representation.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Output: Vector(4, 6)

# Explanation:
# - `__add__` allows `+` to be used between `Vector` instances.
# - `__str__` defines how the object is printed.


#------------------------------------------------#
#   7. Inheritance and Method Overriding
#------------------------------------------------#
# Child classes can override methods from the parent class, replacing or extending functionality.

class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!

# Explanation:
# - `Dog` and `Cat` both override the `speak` method to provide specific sounds.


#------------------------------------------------#
#   8. Encapsulation with Private Methods
#------------------------------------------------#
# Prefixing a method with `__` makes it harder to access from outside the class (name mangling).
# This is a convention to indicate that the method is intended for internal use only.

class Secret:
    def __init__(self, message):
        self.__message = message  # Private attribute

    def __reveal(self):  # Private method
        return f"The secret message is: {self.__message}"

secret = Secret("Python is fun!")
# secret.__reveal()  # Raises AttributeError

# Explanation:
# - `__message` and `__reveal` are private and not accessible directly from outside the class.


#------------------------------------------------#
#   9. Using `isinstance` and `issubclass`
#------------------------------------------------#
# `isinstance` checks if an object is an instance of a particular class or tuple of classes.
# `issubclass` checks if a class is a subclass of another class.

print(isinstance(dog, Dog))          # Output: True
print(isinstance(dog, Animal))       # Output: True
print(issubclass(Dog, Animal))       # Output: True
print(issubclass(Dog, Cat))          # Output: False

# Explanation:
# - `isinstance(dog, Dog)` checks if `dog` is an instance of `Dog`.
# - `issubclass(Dog, Animal)` checks if `Dog` is a subclass of `Animal`.


#------------------------------------------------#
#   10. Class Variables vs. Instance Variables
#------------------------------------------------#
# Class variables are shared across all instances of a class, while instance variables are unique to each instance.

class Employee:
    company = "TechCorp"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

e1 = Employee("Alice")
e2 = Employee("Bob")
print(e1.company)  # Output: TechCorp
print(e2.company)  # Output: TechCorp
e1.company = "NewCorp"
print(e1.company)  # Output: NewCorp
print(e2.company)  # Output: TechCorp

# Explanation:
# - `company` is a class variable shared across all instances.
# - Modifying `company` on `e1` creates an instance variable for `e1` without affecting `e2`.


#------------------------------------------------#
#   11. Abstract Base Classes (ABCs)
#------------------------------------------------#
# Abstract base classes define methods that must be implemented in subclasses.
# They cannot be instantiated directly and are used to enforce structure in subclasses.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # Output: Woof!

# Explanation:
# - `Animal` is an abstract base class, and `speak` is an abstract method.
# - `Dog` must implement `speak` to be instantiable.


#------------------------------------------------#
#   Summary of Advanced Class Concepts
#------------------------------------------------#
# - **Inheritance**: Allows one class to inherit attributes and methods from another.
# - **super()**: Calls methods from a parent class in a child class.
# - **Class Methods**: Use `@classmethod` for methods that operate on the class itself.
# - **Static Methods**: Use `@staticmethod` for methods that don’t interact with instance or class
