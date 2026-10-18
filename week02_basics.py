"""
Week 2: Python Fundamentals
Course: The Joy of Computing using Python - NPTEL

Topics covered:
1. Variables and assignment
2. Displaying output
3. Taking user input
4. Sequential execution
5. Type conversion
6. Arithmetic operations
7. Conditional statements
8. For loops
9. While loops
"""


# --------------------------------------------------
# 1. VARIABLES AND PRINTING OUTPUT
# --------------------------------------------------

name = "Amit"
age = 18

print("Hello", name)
print("Age:", age)


# --------------------------------------------------
# 2. SEQUENTIAL EXECUTION
# --------------------------------------------------

a = 1

print("First value:", a)

a = a + 1
print("Second value:", a)

a = a + 1
print("Third value:", a)


# --------------------------------------------------
# 3. TAKING INPUT FROM THE USER
# --------------------------------------------------

name = input("What is your name? ")

print("Hello", name)


# --------------------------------------------------
# 4. TAKING NUMERICAL INPUT
# --------------------------------------------------

cost = int(input("Enter the cost: "))

print("The cost is:", cost)


# --------------------------------------------------
# 5. BASIC ARITHMETIC OPERATIONS
# --------------------------------------------------

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print("Addition:", number1 + number2)
print("Subtraction:", number1 - number2)
print("Multiplication:", number1 * number2)
print("Division:", number1 / number2)


# --------------------------------------------------
# 6. CALCULATING THE PRICE AFTER A DISCOUNT
# --------------------------------------------------

cost = float(input("Enter the original price: "))

discount = 10

discount_amount = cost * discount / 100
final_price = cost - discount_amount

print("Original price:", cost)
print("Discount percentage:", discount, "%")
print("Final price:", final_price)


# --------------------------------------------------
# 7. CONDITIONAL STATEMENTS
# --------------------------------------------------

choice = int(input("Enter a number (1, 2, or 3): "))

if choice == 1:
    print("You entered one.")

if choice == 2:
    print("You entered two.")

if choice == 3:
    print("You entered three.")


# --------------------------------------------------
# 8. INTRODUCTION TO FOR LOOPS
# --------------------------------------------------

for i in range(5):
    print(i)


# --------------------------------------------------
# 9. USING A FOR LOOP WITH A MESSAGE
# --------------------------------------------------

for i in range(2):
    print("Hello! You are at iteration", i)


# --------------------------------------------------
# 10. MULTIPLICATION USING A LOOP
# --------------------------------------------------

for i in range(11):
    print(i * 2)


# --------------------------------------------------
# 11. SUM OF NUMBERS USING A LOOP
# --------------------------------------------------

answer = 0

for i in range(5):
    answer = answer + i

print("Sum:", answer)


# --------------------------------------------------
# 12. MULTIPLICATION TABLE
# --------------------------------------------------

table = int(input("Which multiplication table do you want? "))

for i in range(11):
    print(table, "x", i, "=", table * i)


# --------------------------------------------------
# 13. INTRODUCTION TO WHILE LOOPS
# --------------------------------------------------

count = 1

while count <= 5:
    print("Count:", count)
    count = count + 1


# --------------------------------------------------
# END OF WEEK 2
# --------------------------------------------------
