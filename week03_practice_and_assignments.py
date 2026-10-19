# ============================================
# THE JOY OF COMPUTING USING PYTHON
# WEEK 3: PRACTICE AND ASSIGNMENTS
# ============================================


# --------------------------------------------
# 1. BASIC DATA ANALYSIS
# --------------------------------------------

from statistics import mean

estimates = [
    1000, 1010, 1786, 2000, 2500,
    3000, 3500, 4000, 5000, 6000
]

estimates.sort()

print("Sorted estimates:")
print(estimates)

trim_value = int(0.1 * len(estimates))

if trim_value > 0:
    remaining = estimates[trim_value:-trim_value]
else:
    remaining = estimates

print("Remaining estimates:")
print(remaining)

print("Mean:")
print(mean(remaining))


# --------------------------------------------
# 2. MATPLOTLIB
# --------------------------------------------

# Install Matplotlib if necessary:
# pip install matplotlib

def plot_example():

    import matplotlib.pyplot as plt

    x = [1, 2, 3, 4]
    y = [1, 4, 9, 16]

    plt.plot(x, y, "ro")

    plt.title("Example Plot")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")

    plt.show()


# Uncomment to display the graph:
# plot_example()


# --------------------------------------------
# ASSIGNMENT 1: RUNNER FINISHING TIMES
# --------------------------------------------

def runner_assignment():

    times = input(
        "Enter runner finishing times separated by spaces: "
    ).split()

    if not times:
        print("Please enter at least one finishing time.")
        return

    finishing_times = []

    for time in times:
        finishing_times.append(float(time))

    fastest_time = min(finishing_times)

    print("Fastest finishing time:", fastest_time)


# --------------------------------------------
# ASSIGNMENT 2: WEATHER TEMPERATURES
# --------------------------------------------

def temperature_assignment():

    temperatures = input(
        "Enter temperatures separated by spaces: "
    ).split()

    total = 0

    for temperature in temperatures:
        total += int(float(temperature))

    print("Sum of integer temperature values:", total)


# --------------------------------------------
# ASSIGNMENT 3: COURIER PACKAGE WEIGHTS
# --------------------------------------------

def package_weight_assignment():

    weights_input = input(
        "Enter package weights separated by spaces: "
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
            count += 1

    print("Average package weight:", average)

    print("Number of packages above average:", count)


# --------------------------------------------
# RUNNING THE ASSIGNMENTS
# --------------------------------------------

# Uncomment ONE function call at a time to run
# the assignment you want to practise.

# runner_assignment()

# temperature_assignment()

# package_weight_assignment()
