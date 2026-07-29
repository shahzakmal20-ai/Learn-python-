# List Slicing & Modification Swap
# Task:
# Write a program that takes a list of 6 items representing sensor data, splits it into two halves, modifies both halves using only list methods and slicing, and combines them.

# Create a list:

# readings = [10, 20, 30, 40, 50, 60]

# Create two sublists using slicing:

# first_half containing the first 3 elements ([10, 20, 30])

# second_half containing the last 3 elements ([40, 50, 60])

# Reverse the first_half list using a list method.

# Replace the last element of second_half with 100 using index assignment (second_half[-1] = ... or second_half[2] = ...).

# Combine both modified halves into a brand-new list called final_readings using list concatenation (+).

# Print final_readings.


readings = [10, 20, 30, 40, 50, 60]
length = int(len(readings)/2)
first_half = readings[:length]
second_half = readings[length:]

print("First half of the readings:", first_half)
print("Second half of the readings:", second_half)

first_half.sort(reverse=True)

second_half[-1] = 100

print("First half after sorting in descending order:", first_half)
print("Second half after inserting 100 at the end:", second_half)


final_readings = first_half + second_half
print("Final readings after combining both halves:", final_readings)

# readings = [10, 20, 30, 40, 50, 60]
# reading1 = readings[0:3]
# reading2 = readings[3:len(readings)]

# print("Reading 1:", reading1)
# print("Reading 2:", reading2)