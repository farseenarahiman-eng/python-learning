# ============================================
# THE JOY OF COMPUTING USING PYTHON
# WEEK 3: RANDOM MODULE AND FILE HANDLING
# ============================================

import random


# 1. GENERATING RANDOM NUMBERS

print("Random integer:")
print(random.randint(1, 5))

print("\nRandom decimal:")
print(random.random())

print("\nRandom odd number:")
print(random.randrange(1, 10, 2))

print("\nRandom even number:")
print(random.randrange(2, 11, 2))


# 2. SELECTING A RANDOM ELEMENT

my_list = [11, 45, 67, 89]

print("\nRandom element:")
print(random.choice(my_list))


# 3. CHOOSING A RANDOM WORD

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


# 4. JUMBLING A WORD

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


# 5. FILE HANDLING

# Writing to a file

with open("file1.txt", "w") as myfile:
    myfile.write("I am fine.")


# Reading from a file

with open("file1.txt", "r") as myfile:
    content = myfile.read()

print("\nFile contents:")
print(content)
