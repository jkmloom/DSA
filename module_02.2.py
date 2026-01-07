# *************************
# 2.2 Data Types in Python
# *************************
#  You’ve already seen Numerical and Sequential data types. Now let’s add some more important categories in Python
# ------------------------------------------------------------------

# 🔹 Set
# - A set is an unordered collection of unique items.
# - It automatically removes duplicates.
# - You can perform mathematical set operations like union, intersection, and difference.
# Example:
fruits = {"apple", "banana", "cherry", "apple"}  # duplicate "apple" will be removed
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)          # {1, 2, 3, 4, 5}
print("Intersection:", a & b)   # {3}
print("Difference:", a - b)     # {1, 2}
# ------------------------------------------------------------------

# 🔹 Dictionary
# - A dictionary is an unordered collection of key-value pairs.
# - Keys must be unique and immutable (like strings, numbers, tuples).
# - Values can be of any type.
# - Think of it like a real-world dictionary: you look up a word (key) to find its meaning (value).
# Example:
student = {
    "name": "Jatin",
    "age": 25,
    "skills": ["Python", "Design", "Art"]
}

print(student["name"])   # Access value by key → Jatin
print(student["skills"]) # Output: ['Python', 'Design', 'Art']

# Adding a new key-value pair
student["country"] = "India"
print(student)

# Iterating through dictionary
for key, value in student.items():
    print(key, ":", value)
# ------------------------------------------------------------------

# - Numerical → int, float, complex
# - Sequential → str, list, tuple, range
# - Set → set, frozenset (immutable set)
# - Mapping → dict
# 👉 Sets are great for uniqueness and mathematical operations.
# 👉 Dictionaries are perfect for structured data with key-value relationships.