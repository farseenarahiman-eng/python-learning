# ============================================================
# THE JOY OF COMPUTING USING PYTHON
# WEEK 3: PRACTICE AND ASSIGNMENTS
# ============================================================
#
# Topics covered:
# 1. List Operations
# 2. Random Module
# 3. File Handling
# 4. Basic Data Analysis
# 5. Data Visualisation using Matplotlib
# 6. Jumbled Word Game
# 7. Runner Finishing Times Assignment
# 8. Weather Station Temperatures Assignment
# 9. Package Weights Assignment
#
# Author: Your Name
# ============================================================


# ------------------------------------------------------------
# 1. LIST OPERATIONS
# ------------------------------------------------------------

print("1. LIST OPERATIONS")

ages = [
    12, 23, 34, 42, 15, 57, 12, 16, 25,
    23, 82, 57, 7, 3, 2, 3, 1, 20
]

# Display the original list
print("Original list:", ages)

# Count the occurrences of an element
print("Count of 25:", ages.count(25))
print("Count of 12:", ages.count(12))
print("Count of 70:", ages.count(70))

# Find the length of the list
print("Length of the list:", len(ages))

# Sort the list in ascending order
ages.sort()
print("Sorted list:", ages)

# Reverse the list
ages.reverse()
print("Reversed list:", ages)


# ------------------------------------------------------------
# 2. LIST SLICING
# ------------------------------------------------------------

print("\n2. LIST SLICING")

students = [
    "Arun",
    "Rajesh",
    "Harish",
    "Akanksha",
    "Lakshmi",
    "Varsha"
]

# Sort the names alphabetically
students.sort()
print("Sorted students:", students)

# Insert a new name at index 0
students.insert(0, "Joc")
print("After insertion:", students)

# Display elements from index 1 to index 4
print("students[1:5]:", students[1:5])

# Display the entire list
print("students[:]:", students[:])

# Display elements from index 4 onwards
print("students[4:]:", students[4:])

# Display elements from the beginning to index 1
print("students[:2]:", students[:2])


# ------------------------------------------------------------
# 3. RANDOM MODULE
# ------------------------------------------------------------

import random

print("\n3. RANDOM MODULE")

# Generate a random integer between 1 and 5
print("Random integer:", random.randint(1, 5))

# Generate a random integer from 1 to 9
print("Random range value:", random.randrange(1, 10))

# Generate a random decimal between 0 and 1
print("Random decimal:", random.random())

# Generate a random odd number between 1 and 10
print("Random odd number:", random.randrange(1, 10, 2))

# Generate a random even number between 2 and 10
print("Random even number:", random.randrange(2, 11, 2))

# Select a random element from a list
my_list = [11, 45, 67, 89]
print("Random list element:", random.choice(my_list))


# ------------------------------------------------------------
# 4. JUMBLED WORD GAME
# ------------------------------------------------------------

print("\n4. JUMBLED WORD GAME")

words = [
    "rainbow",
    "computer",
    "science",
    "programming",
    "mathematics"
]


def choose():
    """Choose a random word from the word list."""
    return random.choice(words)


def jumble(word):
    """Randomly rearrange the letters of a word."""
    letters = random.sample(word, len(word))
    return "".join(letters)


# Demonstrate choosing and jumbling a word
picked_word = choose()
jumbled_word = jumble(picked_word)

print("Jumbled word:", jumbled_word)
print("Original word:", picked_word)


# ------------------------------------------------------------
# 5. BASIC DATA ANALYSIS
# ------------------------------------------------------------

print("\n5. BASIC DATA ANALYSIS")

from statistics import mean


def trimmed_mean(values):
    """
    Sort the values, remove the lowest and highest 10%,
    and calculate the mean of the remaining values.
    """
    if not values:
        raise ValueError("The list cannot be empty.")

    if not all(isinstance(value, (int, float)) for value in values):
        raise TypeError("All values must be numbers.")

    sorted_values = sorted(values)

    trim_value = int(0.1 * len(sorted_values))

    if trim_value == 0:
        remaining_values = sorted_values
    else:
        remaining_values = sorted_values[trim_value:-trim_value]

    return mean(remaining_values)


# Example data
estimates = [1000, 1010, 1786, 2000, 2500, 3000, 3500, 4000, 5000, 6000]

print("Original estimates:", estimates)
print("Trimmed mean:", trimmed_mean(estimates))


# ------------------------------------------------------------
# 6. DATA VISUALISATION USING MATPLOTLIB
# ------------------------------------------------------------

# Install Matplotlib in your Python environment if necessary:
# pip install matplotlib

def plot_example():
    """Create a simple line graph using Matplotlib."""
    import matplotlib.pyplot as plt

    # Example 1: Plot a list of values
    values = [1, 2, 3, 4]

    plt.plot(values)
    plt.title("Simple Line Plot")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()

    # Example 2: Plot specified x and y coordinates
    x_values = [1, 2, 3, 4]
    y_values = [1, 4, 9, 16]

    plt.plot(x_values, y_values, "ro")
    plt.title("Plot of Squared Values")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.show()


# To display the graphs, uncomment the following line:
# plot_example()


# ------------------------------------------------------------
# 7. ASSIGNMENT 1: RUNNER FINISHING TIMES
# ------------------------------------------------------------

def runner_assignment():
    """
    Accept space-separated finishing times and find
    the minimum finishing time.
    """
    times = input(
        "\nEnter runner finishing times separated by spaces: "
    ).split()

    if not times:
        print("Please enter at least one finishing time.")
        return

    finishing_times = []

    for time in times:
        finishing_times.append(float(time))

    fastest_time = min(finishing_times)

    print("Fastest finishing time:", fastest_time, "seconds")


# ------------------------------------------------------------
# 8. ASSIGNMENT 2: WEATHER STATION TEMPERATURES
# ------------------------------------------------------------

def temperature_assignment():
    """
    Accept space-separated temperatures, convert each
    temperature to its integer part, and calculate the sum.
    """
    temperatures = input(
        "\nEnter temperatures separated by spaces: "
    ).split()

    total = 0

    for temperature in temperatures:
        total = total + int(float(temperature))

    print("Sum of integer temperature values:", total)


# ------------------------------------------------------------
# 9. ASSIGNMENT 3: COURIER PACKAGE WEIGHTS
# ------------------------------------------------------------

def package_weight_assignment():
    """
    Accept space-separated package weights, calculate
    their average, and count weights above the average.
    """
    weights_input = input(
        "\nEnter package weights separated by spaces: "
    ).split()

    if not weights_input:
        print("Please enter at least one package weight.")
        return

    weights = []

    for weight in weights_input:
        weights.append(float(weight))

    average = sum(weights) / len(weights)

    count = 0

    for weight in weights:
        if weight > average:
            count = count + 1

    print("Average package weight:", average)
    print("Number of packages above average:", count)


# ------------------------------------------------------------
# 10. FILE HANDLING
# ------------------------------------------------------------

def file_handling_example():
    """
    Demonstrate writing to and reading from a text file.
    This function creates a file named file1.txt.
    """

    # Write mode: creates the file or replaces its contents
    with open("file1.txt", "w") as myfile:
        myfile.write("I am fine.")

    # Read mode: reads the contents of the file
    with open("file1.txt", "r") as myfile:
        content = myfile.read()

    print("File contents:", content)


# ------------------------------------------------------------
# END OF WEEK 3 PRACTICE FILE
# ------------------------------------------------------------

print("\nWeek 3 practice file loaded successfully!")

# To run an assignment, remove the # from its function call.
#
# runner_assignment()
# temperature_assignment()
# package_weight_assignment()
#
# To demonstrate file handling:
# file_handling_example()
#
# To display the graphs:
# plot_example()
