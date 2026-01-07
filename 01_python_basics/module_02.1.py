# *************************
# 2.1 Data Types in Python
# *************************

# 🔹 1. Numerical Data Types
# Numerical types are used to store numbers. Python provides three main numerical types:
# ------------------------------------------------------------------
# - int (Integer)
# Whole numbers, positive or negative, without decimals.
# Example: x = 10

# - float (Floating Point)
# Numbers with decimals.
# Example: pi = 3.14

# - complex (Complex Numbers)
# Numbers with a real and imaginary part.
# Example: z = 2 + 3j

# 👉 These types allow mathematical operations like addition, subtraction, multiplication, division, etc.
# ------------------------------------------------------------------

# 🔹 2. Sequential Data Types
# Sequential types store collections of items in a specific order. Python provides several sequential types:
# ------------------------------------------------------------------
# - str (String)
# A sequence of characters enclosed in quotes.
# Example: name = "Python"

# - list
# An ordered, mutable collection of items.
# Example: numbers = [1, 2, 3, 4]

# - tuple
# An ordered, immutable collection of items.
# Example: coordinates = (10, 20)

# - range
# Represents a sequence of numbers, often used in loops.
# Example: range(5) → produces numbers 0, 1, 2, 3, 4

# 👉 Sequential types let you access elements by index, slice them, and iterate over them.
# ------------------------------------------------------------------

# Numerical Data Types
a = 10          # int
b = 3.14        # float
c = 2 + 3j      # complex

print("Integer:", a)
print("Float:", b)
print("Complex:", c)

# Sequential Data Types
text = "Hello Python"         # string
numbers = [1, 2, 3, 4, 5]     # list
coordinates = (10, 20)        # tuple
sequence = range(5)           # range

print("String:", text)
print("List:", numbers)
print("Tuple:", coordinates)
print("Range:", list(sequence))  # convert range to list for display