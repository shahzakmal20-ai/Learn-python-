# ===================================================FUNCTIONS===================================================

def print_greeting():
    """
    This function prints a greeting message.
    """
    print("Hello!", end=" ") #this will print the message without a newline at the end
    print("Welcome to the Python learning journey.")


def calculate_sum(a, b):
    """
    This function takes two numbers as input and returns their sum.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b

def argument_example(a,b=1):
    multiply = a*b
    print("The arguments passed are:", a, b)
    print("The product of the arguments is:", multiply)

print_greeting()
# sum_result = calculate_sum(5, 10)
# print("The sum of 5 and 10 is:", sum_result)
# print("The sum of 5 and 10 is:", calculate_sum(5, 10))


# argument_example(5)

# argument_example(5, 2)


# ======================PRACTICE OF FUNCTIONS========================

# def print_listLength(list1):
#     """
#     This function takes a list as input and prints its length.
    
#     Parameters:
#     list1 (list): The list whose length is to be printed.
#     """
#     print("The length of the list is:", len(list1))

# def print_listElements(list1):
#     print("The elements of the list are:")
#     for element in list1:
#         print(element, end=" ")
#     print()  # Print a newline at the end

# list1 = [1, 2, 3, 4, 5]
# print_listLength(list1)
# print_listElements(list1)

# def factorial(n):
#     """
#     This function calculates the factorial of a given number.
    
#     Parameters:
#     n (int): The number whose factorial is to be calculated.
    
#     Returns:
#     int: The factorial of the number.
#     """
#     if n < 0:
#         print("Factorial is not defined for negative numbers.")
#         return None 
#     elif n == 0 or n == 1:
#         print("The factorial of", n, "is 1.")
#         return 1
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         print("The factorial of", n, "is", result)  
#         return result



# factorial(6)  # Example usage of the factorial function


def convert_currency(amount, from_currency, to_currency):
    """
    This function converts an amount from one currency to another.
    
    Parameters:
    amount (float): The amount of money to convert.
    from_currency (str): The currency code of the original currency.
    to_currency (str): The currency code of the target currency.
    
    Returns:
    float: The converted amount in the target currency.
    """
    # For simplicity, let's assume a fixed conversion rate for demonstration purposes
    conversion_rates = {
        'PKR': 1.0,
        'EUR': 0.85,
        'GBP': 0.75,
        'INR': 74.0
    }
    
    if from_currency not in conversion_rates or to_currency not in conversion_rates:
        print("Currency not supported.")
        return None
    
    # Convert the amount to USD first, then to the target currency
    amount_in_usd = amount / conversion_rates[from_currency]
    converted_amount = amount_in_usd * conversion_rates[to_currency]
    
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
    return converted_amount

convert_currency(1000, 'PKR', 'EUR')  # Example usage of the currency conversion function