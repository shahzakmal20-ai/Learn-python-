# #  Problem: Server Log Time Breakdown Engine

# ### Scenario:
# You are building a backend utility that processes execution time logs. The system outputs execution times in total seconds, but human operators need to see the breakdown in Hours, Minutes, and Remaining Seconds.

# ### Tasks & Requirements:
# 1. Prompt the user to enter `total_seconds` as an integer (e.g., 3815).
# 2. Calculate total `hours` using integer division `//` (1 hour = 3600 seconds).
# 3. Find the leftover seconds after hours using the modulo operator `%`.
# 4. Calculate `minutes` from the leftover seconds using integer division `//` (1 minute = 60 seconds).
# 5. Find the final remaining `seconds` using modulo `%`.
# 6. Print the formatted result:
#    `Hours: H | Minutes: M | Seconds: S`

# ### Test Case:
# Input: 3815
# Expected Output: Hours: 1 | Minutes: 3 | Seconds: 35



print("\n--- Server Log Time Breakdown Engine ---")
# Step 1: Prompt user for total seconds
total_seconds = int(input("Enter total execution time in seconds: "))

hours = total_seconds / 3600
hours = int(hours) 
print("Hours: ", hours)
remaining_seconds = total_seconds - (hours * 3600) 
print("Remaining Seconds after hours: ", remaining_seconds) 
minutes = remaining_seconds / 60
minutes = int(minutes)
print("Minutes: ", minutes)
seconds = remaining_seconds - (minutes * 60)
print("Seconds: ", seconds)                       

# # 🛒 Problem2: Grocery Store Discount Calculator

# ### Scenario:
# A local grocery store wants a small Python script to calculate the total bill for a customer, check if they qualify for a discount, and display their final payable amount.

# ### Tasks & Requirements:
# 1. Ask the user for:
#    - Item price (float)
#    - Quantity purchased (int)
# 2. Calculate the raw_total (price multiplied by quantity).
# 3. Create a boolean variable is_eligible that evaluates to True if raw_total is greater than 50.0, otherwise False.
# 4. Calculate a 10% discount amount based on raw_total.
# 5. Compute the final_bill after subtracting the discount if eligible.
#    (Hint: You can use logic like final_bill = raw_total - (discount * is_eligible) since True evaluates to 1 and False evaluates to 0 in arithmetic).
# 6. Print the results clearly showing:
#    - Raw Total
#    - Eligibility Status (True/False)
#    - Final Bill


price = float(input("Enter item price: "))
quantity = int(input("Enter quantity purchased: "))
raw_total = price * quantity
is_eligible = raw_total > 50.0
discount = raw_total *(10 / 100)
final_bill = raw_total - discount * is_eligible
print("Raw Total: $", raw_total)
print("Eligibility for Discount:", is_eligible)  

print(22.2*True)