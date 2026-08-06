# ===================================RECURSION===================================

# n = 1
# def recursive_function(n):
#     if n == 10:
#         return
#     else:
#         print(n)
#         recursive_function(n + 1)
#     print("This is the end of the recursion.")
# recursive_function(n)



# FACTORIAL WITH RECURSION


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(0))  # Output: 120



# SUM OF N WITH RECURSION

# def sum_of_n(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum_of_n(n - 1)

# print(sum_of_n(5))  # Output: 15


# PRINTING A LIST WITH RECURSION

list1 = ["apple", "banana", "cherry", "date"]
def print_list(list1, idx=0):
    if idx == len(list1):
        return 0
    print(list1[idx])
    return print_list(list1, idx + 1)


print_list(list1)