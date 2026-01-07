# **********************
# 2.4 Typecasting in Python
# **********************

# - Typecasting means converting one data type into another.
# - Python provides built-in functions for typecasting:
# - int() → converts to integer
# - float() → converts to float
# - str() → converts to string
# - bool() → converts to Boolean

# Converting string to int
num_str = "100"
num_int = int(num_str)
print(num_int + 50)    # Output: 150

# Converting float to int
pi = 3.14
pi_int = int(pi)
print(pi_int)          # Output: 3

# Converting int to float
age = 25
age_float = float(age)
print(age_float)       # Output: 25.0

# Converting values to Boolean
print(bool(0))         # Output: False
print(bool(1))         # Output: True
print(bool(""))        # Output: False
print(bool("Hello"))   # Output: True