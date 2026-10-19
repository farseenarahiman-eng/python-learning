# ============================================
# THE JOY OF COMPUTING USING PYTHON
# WEEK 3: LISTS
# ============================================


# 1. CREATING A LIST

shopping = ["Bread", "Coffee", "Sugar"]

print("Shopping list:")
print(shopping)


# 2. ACCESSING ELEMENTS USING A LOOP

print("\nShopping items using a loop:")

for item in shopping:
    print(item)


# 3. USING RANGE AND INDEXING

print("\nShopping items using indexes:")

for i in range(len(shopping)):
    print(shopping[i])


# 4. APPENDING AN ELEMENT

shopping.append("Curd")

print("\nAfter appending Curd:")
print(shopping)


# 5. INSERTING AN ELEMENT

shopping.insert(1, "Oil")

print("\nAfter inserting Oil:")
print(shopping)


# 6. COUNTING ELEMENTS

ages = [
    12, 23, 34, 42, 15, 57, 12, 16, 25,
    23, 82, 57, 7, 3, 2, 3, 1, 20
]

print("\nCount of 25:", ages.count(25))
print("Count of 12:", ages.count(12))
print("Count of 70:", ages.count(70))


# 7. FINDING THE LENGTH

print("\nNumber of ages:", len(ages))


# 8. SORTING A LIST

ages.sort()

print("\nSorted ages:")
print(ages)


# 9. REVERSING A LIST

ages.reverse()

print("\nReversed ages:")
print(ages)


# 10. SORTING STUDENT NAMES

students = [
    "Arun",
    "Rajesh",
    "Harish",
    "Akanksha",
    "Lakshmi",
    "Varsha"
]

students.sort()

print("\nSorted students:")
print(students)


# 11. INSERTING A STUDENT

students.insert(0, "Joc")

print("\nAfter inserting a student:")
print(students)


# 12. LIST SLICING

print("\nFirst four elements:")
print(students[:4])

print("\nElements from index 4 onwards:")
print(students[4:])

print("\nEntire list:")
print(students[:])

print("\nElements from index 1 to index 4:")
print(students[1:5])
