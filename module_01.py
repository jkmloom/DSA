# ******************************************
# 1. 🐍 Variables, Input, and Output in Python
# ******************************************

# 🔹 Variables
# - A variable is like a container that stores data.
# - You give it a name, and it holds a value that you can use or change later.
# - Example: age = 25 → here age is the variable, and 25 is the value stored inside it.
# ------------------------------------------------------------------
# 🔹 Input
# - The input() function lets you take data from the user.
# - Whatever the user types is stored as a string by default.
# - Example: name = input("Enter your name: ")
# ------------------------------------------------------------------
# 🔹 Output
# - The print() function is used to display information to the user.
# - You can print text, numbers, or variables.
# - Example: print("Hello, World!")
# ------------------------------------------------------------------

# Variable assignment
greeting = "Welcome to Python!"

# Output using print()
print(greeting)

# Taking input from the user
name = input("Enter your name: ")
age = input("Enter your age: ")

# Output using variables and user input
print("Hello " + name + "! You are " + age + " years old.")

# Demonstrating numeric input (convert string to integer)
number = int(input("Enter a number: "))
print("The square of your number is:", number * number)

# 📝 What this code does:
# - Stores a message in a variable (greeting) and prints it.
# - Asks the user for their name and age using input().
# - Prints a personalized message using those variables.
# - Shows how to convert input into an integer (int()) and perform a calculation.