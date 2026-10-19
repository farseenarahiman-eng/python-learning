# ============================================
# THE JOY OF COMPUTING USING PYTHON
# WEEK 3: LOOPS AND CONDITIONALS
# ============================================


# 1. BASIC FOR LOOP

print("Numbers from 1 to 10:")

for i in range(1, 11):
    print(i)


# 2. CHECKING DIVISIBILITY

print("\nChecking divisibility:")

for i in range(1, 16):

    if i % 3 == 0:
        print(i, "is divisible by 3")

    elif i % 5 == 0:
        print(i, "is divisible by 5")

    else:
        print(i, "is not divisible by 3 or 5")


# 3. FIZZBUZZ

def fizzbuzz(n):
    """Print FizzBuzz results from 1 to n."""

    for i in range(1, n + 1):

        if i % 3 == 0 and i % 5 == 0:
            print(str(i) + " = FizzBuzz")

        elif i % 3 == 0:
            print(str(i) + " = Fizz")

        elif i % 5 == 0:
            print(str(i) + " = Buzz")

        else:
            print(i)


print("\nFizzBuzz from 1 to 50:")
fizzbuzz(50)
