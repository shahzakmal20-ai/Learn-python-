# ==========================================================
# PYTHON LECTURE 2: STRINGS & CONDITIONAL STATEMENTS

# ----------------------------------------------------------
# 1. String Basics & Escape Sequences
# ----------------------------------------------------------
# Creating strings using single, double, and triple quotes
str1 = "This is a double-quoted string."
str2 = 'This is a single-quoted string.'
str3 = """This is a triple-quoted multi-line string."""

# Handling apostrophes using double quotes
quote_str = "This is Shradha's Python tutorial."

# Escape sequences: \n (newline), \t (tab)
print("--- Escape Sequences ---")
print("Line 1\nLine 2")
print("Name:\tAkmal")

# Concatenation and length
first_name = "Akmal"
last_name = "Shahzad"
full_name = first_name + " " + last_name
print("\nFull Name:", full_name)
print("Length of Full Name:", len(full_name))

# ----------------------------------------------------------
# 2. Indexing & Slicing
# ----------------------------------------------------------
text = "PythonCode"

print("\n--- Indexing & Slicing ---")
# Positive Indexing
print("First character [0]:", text[0])
print("Last character [-1]:", text[-1])

# Slicing: text[start : end] (end index is excluded)
print("Slice [0:6]:", text[0:6])   # 'Python'
print("Slice [6:]:", text[6:])     # 'Code'
print("Negative Slicing [-4:]:", text[-4:]) # 'Code'

# ----------------------------------------------------------
# 3. Common String Functions
# ----------------------------------------------------------
msg = "i am learning python programming"

print("\n--- String Functions ---")
print("Ends with 'programming':", msg.endswith("programming"))
print("Capitalized:", msg.capitalize())
print("Replaced 'python' with 'coding':", msg.replace("python", "coding"))
print("Index of 'python':", msg.find("python"))
print("Count of letter 'a':", msg.count("a"))

# ----------------------------------------------------------
# 4. Conditional Statements (if - elif - else)
# ----------------------------------------------------------
print("\n--- Conditional Statements ---")
light_color = "green"

if light_color == "red":
    print("Stop!")
elif light_color == "yellow":
    print("Look / Slow Down")
elif light_color == "green":
    print("Go!")
else:
    print("Invalid Light Color")

# Note: In Python, 'elif' is used, NOT 'elseif'

# ----------------------------------------------------------
# 5. Nesting & Modulo Checks
# ----------------------------------------------------------
print("\n--- Nesting & Modulo ---")
num = 14

# Check even/odd and positive/negative using nesting
if num >= 0:
    print(f"{num} is Positive")
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
else:
    print(f"{num} is Negative")


# ==========================================================
# 6. PRACTICE PROBLEMS FROM LECTURE 2
# ==========================================================
print("\n==========================================")
print("          PRACTICE PROBLEMS")
print("==========================================")

# Problem 1: WAP to input user's first name & print its length.
print("\n--- Problem 1: First Name Length ---")
user_first_name = input("Enter your first name: ")
print("Length of your first name:", len(user_first_name))

# Problem 2: WAP to find the occurrence of '$' in a String.
print("\n--- Problem 2: Count '$' Symbol ---")
sample_text = "The price is $100 and the fee is $5."
print("Occurrences of '$':", sample_text.count("$"))

# Problem 3: WAP to check if a number entered by the user is odd or even.
print("\n--- Problem 3: Even or Odd Checker ---")
check_num = int(input("Enter an integer: "))
if check_num % 2 == 0:
    print("The number is EVEN.")
else:
    print("The number is ODD.")

# Problem 4: WAP to find the greatest of 3 numbers entered by the user.
print("\n--- Problem 4: Greatest of 3 Numbers ---")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1 >= n2 and n1 >= n3:
    print("Greatest number is:", n1)
elif n2 >= n3:
    print("Greatest number is:", n2)
else:
    print("Greatest number is:", n3)

# Problem 5: WAP to check if a number is a multiple of 7 or not.
print("\n--- Problem 5: Multiple of 7 Checker ---")
mult_num = int(input("Enter a number to check for multiple of 7: "))
if mult_num % 7 == 0:
    print(f"{mult_num} is a MULTIPLE of 7.")
else:
    print(f"{mult_num} is NOT a multiple of 7.")