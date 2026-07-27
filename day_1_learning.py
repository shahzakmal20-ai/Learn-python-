# ==========================================
# PYTHON LECTURE 1: VARIABLES & DATA TYPES
# Course: Python Full Course by Shradha Khapra
# ==========================================

# ------------------------------------------
# 1. Output & Printing
# ------------------------------------------
print("Hello, Python!")
print("Welcome to Lecture 1.")

# ------------------------------------------
# 2. Variables & Data Types
# ------------------------------------------
name = "Akmal"         # String (str)
age = 22               # Integer (int)
cgpa = 3.44            # Float (float)
is_learning = True     # Boolean (bool)
none_var = None        # NoneType (None)

# Printing types
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("CGPA:", cgpa, "| Type:", type(cgpa))
print("Learning:", is_learning, "| Type:", type(is_learning))

# ------------------------------------------
# 3. Operators
# ------------------------------------------
a = 10
b = 3

# Arithmetic Operators
print("\n--- Arithmetic Operators ---")
print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)          # Always yields a float
print("Modulo / Remainder (a % b):", a % b)
print("Power / Exponentiation (a ** b):", a ** b)
# Relational / Comparison Operators
print("\n--- Relational Operators ---")
print("a > b:", a > b)
print("a == b:", a == b)
print("a <= b:", a <= b)

# Logical Operators
print("\n--- Logical Operators ---")
print("True and False:", True and False)
print("True or False:", True or False)
print("not True:", not True)

# ------------------------------------------
# 4. Type Casting (Implicit & Explicit)
# ------------------------------------------
print("\n--- Type Casting ---")
# Implicit (Python automatically converts int to float)
x = 5
y = 2.5
sum_val = x + y
print("5 + 2.5 =", sum_val, "| Type:", type(sum_val))

# Explicit (Converting str to int/float)
num_str = "100"
num_int = int(num_str)
print("Converted string '100' to int:", num_int + 50)


# ==========================================
# 5. PRACTICE PROBLEMS SOLUTIONS
# ==========================================
print("\n==========================================")
print("          PRACTICE PROBLEMS")
print("==========================================")

# Problem 1: The Rectangle Area
print("\n--- Problem 1: Rectangle Area ---")
length = int(input("Enter length of rectangle: "))
width = int(input("Enter width of rectangle: "))
area = length * width
print("Area of rectangle:", area)

# Problem 2: The Coffee Shop Bill
print("\n--- Problem 2: Coffee Shop Bill ---")
coffee_price = float(input("Enter price of coffee ($): "))
sandwich_price = float(input("Enter price of sandwich ($): "))
total_bill = coffee_price + sandwich_price
print("Total Bill: $", total_bill)

# Problem 3: The Age Checker
print("\n--- Problem 3: Age Checker ---")
user_age = int(input("Enter your age: "))
is_adult = user_age >= 18
print("Is eligible / adult (>= 18):", is_adult)