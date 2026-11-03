THE JOY OF COMPUTING USING PYTHON

WEEK 4: NOTES

1. TWO-DIMENSIONAL LISTS

A two-dimensional list is a list that contains other lists.

It is used to represent data in the form of rows and columns.

Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

Accessing Elements

Each element can be accessed using two indexes.

The first index represents the row, and the second index represents the column.

print(matrix[0][0])
print(matrix[1][2])

Output:

1
6

Using Nested Loops

A loop inside another loop is called a nested loop.

Nested loops are useful for accessing all the elements in a two-dimensional list.

for row in matrix:

    for element in row:
        print(element)

2. LIST COMPREHENSION

List comprehension is a short and convenient way of creating lists in Python.

Example:

numbers = [i for i in range(5)]

print(numbers)

Output:

[0, 1, 2, 3, 4]

Creating a Two-Dimensional List

matrix = [[0 for j in range(3)] for i in range(3)]

for row in matrix:
    print(row)

Output:

[0, 0, 0]
[0, 0, 0]
[0, 0, 0]

3. MAGIC SQUARE

A magic square is a square arrangement of numbers in which the sum of every row, every column, and both main diagonals is the same.

This common sum is called the Magic Constant.

For a normal magic square of order n:

Magic Constant = n × (n² + 1) / 2

For example, the magic constant of a 3 × 3 magic square is:

3 × (3² + 1) / 2 = 15

4. RANDOM MODULE

The "random" module is used to generate random numbers and select random elements.

Important functions:

1. "random.random()" – Generates a random floating-point number between 0 and 1.
2. "random.randint(a, b)" – Generates a random integer between a and b, including both.
3. "random.randrange()" – Selects a random number from a specified range.
4. "random.choice()" – Selects a random element from a sequence.
5. "random.sample()" – Selects a specified number of unique elements.
6. "random.shuffle()" – Shuffles the elements of a list.

Example:

import random

numbers = [10, 20, 30, 40, 50]

print(random.randint(1, 10))
print(random.choice(numbers))

5. GUESS THE MOVIE NAME

Guess the Movie Name is a simple word-guessing game.

The program selects a movie name randomly from a list.

The letters of the movie name are hidden using the "*" symbol.

The player guesses one letter at a time.

- If the guessed letter is correct, it is revealed.
- If the guessed letter is incorrect, the program displays a message.
- The player can also try to guess the complete movie name.
- The program keeps track of the players' scores.

6. BIRTHDAY PARADOX

The Birthday Paradox is a probability concept.

It explains that in a group of people, the probability that at least two people share the same birthday is surprisingly high.

For example, in a group of 23 people, the probability of at least two people sharing a birthday is approximately 50.7%.

This assumes 365 equally likely birthdays and ignores leap years.

7. DATE AND TIME

Python provides the "datetime" module to work with dates and times.

Important functions:

- "datetime.date.today()" – Returns the current date.
- "datetime.datetime.now()" – Returns the current date and time.
- "strftime()" – Converts date and time into a formatted string.

Example:

import datetime

today = datetime.date.today()

print(today)

now = datetime.datetime.now()

print(now)

8. WEATHER STATION

A weather station collects temperature readings.

A Python program can be used to process these readings.

Important operations:

- Accepting temperature readings.
- Finding the highest temperature.
- Finding the lowest temperature.
- Calculating the temperature range.

Temperature Range:

Range = Highest Temperature - Lowest Temperature

9. IMPORTANT PYTHON CONCEPTS USED

- Lists
- Two-dimensional lists
- Nested loops
- List comprehension
- Functions
- Conditional statements
- Random module
- Datetime module
- String operations
- List methods
- User input and output
