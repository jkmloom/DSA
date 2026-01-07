# *************************
# 2.3 Data Types in Python
# *************************

# 🔹 Boolean in Python
# - A Boolean represents one of two values: True or False.
# - It’s often used in conditions, comparisons, and logical operations.
# - Booleans are a subtype of integers (True is 1, False is 0).

# Boolean values
is_active = True
is_logged_in = False

print(is_active)       # Output: True
print(is_logged_in)    # Output: False

# Boolean from comparison
x = 10
y = 5
print(x > y)           # Output: True
print(x == y)          # Output: False

# Boolean in condition
if is_active:
    print("The system is active!")
else:
    print("The system is inactive.")
# ------------------------------------------------------------------