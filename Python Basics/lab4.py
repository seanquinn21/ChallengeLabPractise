# Task 1: Open `task1.ipynb` and add a cell that prints `Hello World!`.

print("Hello World!")


# Task 2: Finish the code for `RandomNumberGeneratorClass()` using the `random` package
#         to generate a random integer within a specified range.

import random

class RandomNumberGeneratorClass:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def generate(self):
        return random.randint(self.min_value, self.max_value)

# Example usage:
rng = RandomNumberGeneratorClass(1, 10)
print(rng.generate())  # Prints a random number between 1 and 10


# Task 3: Write a program that asks the user for their name and appends it to `task3.txt`.

name = input("Enter your name: ")
with open("task3.txt", "a") as file:
    file.write(name + "\n")


# Task 4: Write a program that reads each name from `task3.txt` and prints it.

with open("task3.txt", "r") as file:
    for line in file:
        print(line.strip())  # Prints each name on a new line


# Task 5: Continuously ask the user for names and write each name to `task5.csv`.
#         Stop when the user types "quit". Then read and print all names from the CSV.

import csv

with open("task5.csv", "w", newline="") as file:
    writer = csv.writer(file)
    while True:
        name = input("Enter a name (type 'quit' to stop): ")
        if name.lower() == "quit":
            break
        writer.writerow([name])

# Read and print names from the CSV
with open("task5.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])


# Task 6: Given an 8x8 numpy array of ones, set all inner elements to zero,
#leaving only the border as ones.

import numpy as np

arr = np.ones((8, 8))
arr[1:-1, 1:-1] = 0  # Set inner elements to zeroas
print(arr)


[[1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 0. 0. 0. 1.]
 [1. 0. 0. 0. 0. 0. 0. 1.]
 [1. 0. 0. 0. 0. 0. 0. 1.]
 [1. 0. 0. 0. 0. 0. 0. 1.]
 [1. 0. 0. 0. 0. 0. 0. 1.]
 [1. 0. 0. 0. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1.]]


# Task 7: Generate sine and cosine waves using numpy, and save them as
#         `task7_sin.npy` and `task7_cos.npy`.

import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

np.save("task7_sin.npy", y_sin)
np.save("task7_cos.npy", y_cos)


# Task 8: Load the `.npy` files from Task 7 and plot the sine and cosine waves.

import numpy as np
import matplotlib.pyplot as plt

y_sin = np.load("task7_sin.npy")
y_cos = np.load("task7_cos.npy")
x = np.linspace(0, 2 * np.pi, 100)

plt.plot(x, y_sin, label="Sine Wave")
plt.plot(x, y_cos, label="Cosine Wave")
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Sine and Cosine Waves")
plt.legend()
plt.show()


# Task 9: Load data from `task9.csv` and plot it using `matplotlib`.

import csv
import matplotlib.pyplot as plt

x = []
y = []

with open("task9.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Data from task9.csv")
plt.show()


# Task 10: Modify the graph from Task 9 to improve its appearance by adjusting colors,
#          line styles, and adding a legend.

import csv
import matplotlib.pyplot as plt

x = []
y = []

with open("task9.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.plot(x, y, color="blue", linestyle="--", marker="o", label="Data Line")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Tidied Graph from task9.csv")
plt.legend()
plt.grid(True)  # Adds a grid for better readability
plt.show()

