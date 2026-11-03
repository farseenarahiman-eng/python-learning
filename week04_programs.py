============================================

THE JOY OF COMPUTING USING PYTHON

WEEK 4: MAIN PROGRAMS

============================================

--------------------------------------------------

1. CREATING A TWO-DIMENSIONAL LIST

--------------------------------------------------

matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print("Two-dimensional list:")

for row in matrix:
print(row)

--------------------------------------------------

2. ACCESSING ELEMENTS USING NESTED LOOPS

--------------------------------------------------

print("\nMatrix elements:")

for i in range(len(matrix)):

for j in range(len(matrix[i])):
    print(matrix[i][j], end=" ")

print()

--------------------------------------------------

3. CREATING A MATRIX USING LIST COMPREHENSION

--------------------------------------------------

n = 3

matrix = [
[0 for j in range(n)]
for i in range(n)
]

print("\nMatrix created using list comprehension:")

for row in matrix:
print(row)

--------------------------------------------------

4. MAGIC SQUARE

--------------------------------------------------

def magic_square(n):
"""Create a magic square of odd order n."""

if n < 1 or n % 2 == 0:
    print("Please enter a positive odd number.")
    return

# Create an empty n x n matrix
square = [
    [0 for j in range(n)]
    for i in range(n)
]

# Start from the middle column of the first row
row = 0
col = n // 2

# Fill the numbers from 1 to n*n
for number in range(1, n * n + 1):

    square[row][col] = number

    # Move one row up and one column right
    new_row = (row - 1) % n
    new_col = (col + 1) % n

    # If the position is already occupied,
    # move one row down instead
    if square[new_row][new_col] != 0:

        row = (row + 1) % n

    else:

        row = new_row
        col = new_col

# Display the magic square
print("\nMagic Square:")

for row in square:
    for element in row:
        print(element, end="\t")

    print()

# Calculate the magic constant
magic_constant = n * (n * n + 1) // 2

print("\nMagic Constant:", magic_constant)

Example: 3 x 3 Magic Square

magic_square(3)

--------------------------------------------------

5. RANDOM NUMBER GENERATION

--------------------------------------------------

import random

print("\nRandom floating-point number:")
print(random.random())

print("\nRandom integer:")
print(random.randint(1, 10))

print("\nRandom number from a range:")
print(random.randrange(2, 20, 2))

numbers = [10, 20, 30, 40, 50]

print("\nRandom element:")
print(random.choice(numbers))

--------------------------------------------------

6. RANDOMLY SELECTING AND JUMBLING A WORD

--------------------------------------------------

words = [
"rainbow",
"computer",
"science",
"programming",
"mathematics"
]

def choose():
"""Choose a random word."""

return random.choice(words)

def jumble(word):
"""Randomly rearrange the letters of a word."""

letters = random.sample(word, len(word))

jumbled_word = "".join(letters)

return jumbled_word

picked_word = choose()

print("\nOriginal word:")
print(picked_word)

print("\nJumbled word:")
print(jumble(picked_word))

--------------------------------------------------

7. GUESS THE MOVIE NAME

--------------------------------------------------

movies = [
"Drishyam",
"Bajrangi",
"Anbe Sivam",
"Golmaal",
"Vikram Vedha",
"Vaaranam Aayiram"
]

def create_question(movie):
"""Hide the movie name using stars."""

temp = []

for letter in movie:

    if letter == " ":
        temp.append(" ")

    else:
        temp.append("*")

question = "".join(temp)

return question

def is_present(letter, movie):
"""Check whether the guessed letter is in the movie name."""

return letter.lower() in movie.lower()

def unlock(question, movie, letter):
"""Reveal the correctly guessed letters."""

temp = []

for i in range(len(movie)):

    if movie[i].lower() == letter.lower():
        temp.append(movie[i])

    else:
        temp.append(question[i])

new_question = "".join(temp)

return new_question

def play():
"""Run the two-player movie guessing game."""

player1 = input("Player 1! Enter your name: ")
player2 = input("Player 2! Enter your name: ")

pp1 = 0
pp2 = 0

turn = 0
willing = True

while willing:

    if turn % 2 == 0:
        player = player1

    else:
        player = player2

    print("\n", player, "- Your turn!")

    picked_movie = random.choice(movies)

    question = create_question(picked_movie)

    print("Guess the movie name:", question)

    modified_question = question

    not_solved = True
    guessed_letters = []

    while not_solved:

        letter = input("Enter a letter: ").strip()

        if len(letter) != 1 or not letter.isalpha():
            print("Please enter one alphabet at a time.")
            continue

        if letter.lower() in guessed_letters:
            print("You have already guessed this letter.")
            continue

        guessed_letters.append(letter.lower())

        if is_present(letter, picked_movie):

            modified_question = unlock(
                modified_question,
                picked_movie,
                letter
            )

            print("Updated movie name:", modified_question)

        else:

            print("Letter not found!")

        if modified_question == picked_movie:

            print("You revealed the complete movie name!")

        choice = input(
            "Press 1 to guess the movie or 2 to unlock another letter: "
        )

        if choice == "1":

            answer = input("Your answer: ")

            if answer.strip().lower() == picked_movie.lower():

                print("Correct!")

                if turn % 2 == 0:
                    pp1 += 1

                else:
                    pp2 += 1

                not_solved = False

                print(player1, "Your score:", pp1)
                print(player2, "Your score:", pp2)

            else:

                print("Wrong answer. Try again!")

        elif choice == "2":

            continue

        else:

            print("Invalid choice. Please try again.")

        if not_solved:

            c = input(
                "Press 1 to continue or 0 to quit: "
            )

            if c == "0":

                print("\nFinal Scores:")
                print(player1, "Your score:", pp1)
                print(player2, "Your score:", pp2)

                print("Thanks for playing!")
                print("Have a nice day!")

                willing = False
                not_solved = False

    if willing:
        turn += 1

print("\nGame Over!")

if pp1 > pp2:
    print(player1, "wins!")

elif pp2 > pp1:
    print(player2, "wins!")

else:
    print("The game is a tie!")

Uncomment the following line to play the game:

play()

--------------------------------------------------

8. BIRTHDAY PARADOX

--------------------------------------------------

def birthday_simulation(number_of_people):
"""Check whether two people share a birthday."""

birthdays = []

for i in range(number_of_people):

    birthday = random.randint(1, 365)

    birthdays.append(birthday)

if len(birthdays) != len(set(birthdays)):
    return True

else:
    return False

people = 23
trials = 10000
matches = 0

for i in range(trials):

if birthday_simulation(people):
    matches += 1

probability = matches / trials

print("\nBirthday Paradox")

print("Number of people:", people)
print("Number of trials:", trials)
print("Estimated probability:", probability)

--------------------------------------------------

9. DATE AND TIME

--------------------------------------------------

import datetime

today = datetime.date.today()

print("\nToday's date:")
print(today)

now = datetime.datetime.now()

print("\nCurrent date and time:")
print(now)

print("\nFormatted date:")
print(now.strftime("%d-%m-%Y"))

print("\nCurrent time:")
print(now.strftime("%H:%M:%S"))

--------------------------------------------------

10. WEATHER STATION - TEMPERATURE READINGS

--------------------------------------------------

temperatures = [28, 32, 30, 35, 27, 31]

highest = max(temperatures)
lowest = min(temperatures)

temperature_range = highest - lowest

print("\nWeather Station")

print("Temperature readings:", temperatures)
print("Highest temperature:", highest)
print("Lowest temperature:", lowest)
print("Temperature range:", temperature_range)

--------------------------------------------------

11. FINDING COMMON ELEMENTS

--------------------------------------------------

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []

for item in list1:

if item in list2 and item not in common:
    common.append(item)

print("\nFirst list:", list1)
print("Second list:", list2)
print("Common elements:", common)

--------------------------------------------------

END OF WEEK 4

--------------------------------------------------
