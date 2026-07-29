# ==========================================
# PYTHON LECTURE 3: LISTS & TUPLES
# Full practice code for GitHub repository
# ==========================================

# ------------------------------------------
# 1. LIST BASICS & MUTABILITY
# ------------------------------------------
print("--- 1. LIST BASICS & MUTABILITY ---")

# Creating lists (can store multiple data types)
marks = [94.4, 87.5, 95.0, 66.2, 45.1]
student = ["Karan", 22, 95.5, "Delhi"]

print("Marks list:", marks)
print("List length:", len(marks))
print("Type:", type(marks))

# Accessing elements via indexing
print("First element (index 0):", student[0])
print("Last element (index -1):", student[-1])

# Mutability Demonstration (Lists CAN be changed)
student[0] = "Arjun"
print("Updated student list after name change:", student)
print()


# ------------------------------------------
# 2. LIST SLICING
# ------------------------------------------
print("--- 2. LIST SLICING ---")

nums = [85, 94, 76, 63, 48]

print("Original Nums:", nums)
print("nums[1:4]:", nums[1:4])      # Indices 1, 2, 3
print("nums[:3]:", nums[:3])        # Indices 0 to 2
print("nums[2:]:", nums[2:])        # Index 2 to end
print("Negative Slicing nums[-3:-1]:", nums[-3:-1])
print()


# ------------------------------------------
# 3. LIST METHODS
# ------------------------------------------
print("--- 3. LIST METHODS ---")

list_demo = [2, 1, 3]

# 1. append(val) - adds element at the end
list_demo.append(4)
print("After append(4):", list_demo)

# 2. sort() - sorts in ascending order
list_demo.sort()
print("After sort():", list_demo)

# 3. sort(reverse=True) - sorts in descending order
list_demo.sort(reverse=True)
print("After sort(reverse=True):", list_demo)

# 4. reverse() - reverses the list order
list_demo.reverse()
print("After reverse():", list_demo)

# 5. insert(idx, val) - inserts element at specific index
list_demo.insert(1, 5)
print("After insert(1, 5):", list_demo)

# 6. remove(val) - removes first occurrence of value
list_demo.remove(5)
print("After remove(5):", list_demo)

# 7. pop(idx) - removes element at specific index
list_demo.pop(2)
print("After pop(2):", list_demo)
print()


# ------------------------------------------
# 4. TUPLE BASICS & IMMUTABILITY
# ------------------------------------------
print("--- 4. TUPLE BASICS & IMMUTABILITY ---")

# Creating a tuple (uses parentheses)
tup = (87, 64, 33, 95, 76)
print("Tuple:", tup)
print("Type:", type(tup))

# Single element tuple syntax requirement (MUST use trailing comma)
single_tup = (1,)
not_a_tup = (1) # Interpreted as int by Python
print("Single element tuple type:", type(single_tup))
print("Without comma type:", type(not_a_tup))

# Tuple Immutability:
# Executing tup[0] = 90 will raise a TypeError: 'tuple' object does not support item assignment
print()


# ------------------------------------------
# 5. TUPLE METHODS & SLICING
# ------------------------------------------
print("--- 5. TUPLE METHODS & SLICING ---")

tup_demo = (1, 2, 3, 2, 4, 2)

# Slicing tuples works the same as lists
print("Tuple slice tup_demo[1:4]:", tup_demo[1:4])

# 1. index(val) - returns index of first occurrence
print("Index of value 3:", tup_demo.index(3))

# 2. count(val) - counts total occurrences of value
print("Count of value 2:", tup_demo.count(2))
print()


# ==========================================
# 6. PRACTICE QUESTIONS FROM LECTURE
# ==========================================
print("--- 6. PRACTICE PROBLEMS ---")

# --- Problem 1: Input 3 favorite movies and store in a list ---
print("--> Problem 1: Favorite Movies List")
movies = []

movies.append(input("Enter 1st favorite movie: "))
movies.append(input("Enter 2nd favorite movie: "))
movies.append(input("Enter 3rd favorite movie: "))

print("Your favorite movies list:", movies)
print()


# --- Problem 2: Check if a list is a Palindrome ---
print("--> Problem 2: Check Palindrome List")

list1 = [1, 2, 3, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if list1 == copy_list1:
    print(list1, "-> Is a Palindrome")
else:
    print(list1, "-> Is NOT a Palindrome")


list2 = [1, "abc", "def"]

copy_list2 = list2.copy()
copy_list2.reverse()

if list2 == copy_list2:
    print(list2, "-> Is a Palindrome")
else:
    print(list2, "-> Is NOT a Palindrome")
print()


# --- Problem 3: Count grade 'A' in tuple ---
print("--> Problem 3: Count Grade 'A'")
grades_tuple = ("C", "D", "A", "A", "B", "B", "A")
a_count = grades_tuple.count("A")
print("Number of students with Grade 'A':", a_count)
print()


# --- Problem 4: Sort grades from 'A' to 'D' in a list ---
print("--> Problem 4: Sort Grades List")
grades_list = ["C", "D", "A", "A", "B", "B", "A"]
grades_list.sort()
print("Sorted Grades (A to D):", grades_list)