============================================

THE JOY OF COMPUTING USING PYTHON

WEEK 4: PRACTICE AND ASSIGNMENTS

============================================

--------------------------------------------------

ASSIGNMENT 1: WEATHER STATION TEMPERATURE READINGS

--------------------------------------------------

"""
A weather monitoring application collects temperature
readings continuously.

Write a Python program that:

1. Accepts space-separated temperature readings.
2. Finds the highest and lowest temperature.
3. Calculates the temperature range.
4. If all readings are equal, the range will be 0.
   """

temperatures = input(
"Enter temperature readings separated by spaces: "
).split()

temperatures = [int(value) for value in temperatures]

if len(temperatures) > 0:

highest = temperatures[0]
lowest = temperatures[0]

for temperature in temperatures:

    if temperature > highest:
        highest = temperature

    if temperature < lowest:
        lowest = temperature

temperature_range = highest - lowest

print("Highest temperature:", highest)
print("Lowest temperature:", lowest)
print("Temperature range:", temperature_range)

else:

print("No temperature readings entered.")

--------------------------------------------------

ASSIGNMENT 2: CHECK WHETHER A NUMBER IS PRIME

--------------------------------------------------

"""
Before executing an application, the software checks
whether a given number is a prime number.

Write a Python program that:

1. Accepts a positive integer n.
2. Prints True if n is a prime number.
3. Otherwise, prints False.
   """

n = int(input("\nEnter a positive integer: "))

if n < 2:

print(False)

else:

prime = True

for i in range(2, n):

    if n % i == 0:

        prime = False
        break

print(prime)

--------------------------------------------------

ASSIGNMENT 3: FIND DUPLICATE PRODUCT IDs

--------------------------------------------------

"""
A shopping application records the product IDs viewed
by a customer during a browsing session.

The system needs to determine whether the customer
viewed any product more than once.

Write a Python program that:

1. Accepts space-separated integers representing
   product IDs.
2. Prints True if at least one product ID appears
   more than once.
3. Otherwise, prints False.
   """

products = input(
"\nEnter product IDs separated by spaces: "
).split()

products = [int(value) for value in products]

products.sort()

found = False

for i in range(len(products) - 1):

if products[i] == products[i + 1]:

    found = True
    break

print(found)

--------------------------------------------------

END OF WEEK 4 ASSIGNMENTS

--------------------------------------------------
