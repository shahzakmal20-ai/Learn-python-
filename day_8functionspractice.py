# =============================================PRACTICE QUESTIONS========================================

# WRITE A FUNCTION THAT TAKES INPUT AND RETURE THE NUMBER IS EVEN OR ODD

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"





# number = int(input("Enter a number: "))
# result = even_odd(number)
# print(f"The number {number} is {result}.")



# write a program in which one function takes a list as input and pass to second function which will print the inputed list


def print_list(input_list):
    print("The inputed list is:")
    for item in input_list:
        print(item, end=" ")
    print()  # Print a newline at the end   


def get_list():
    input_list = []
    n = int(input("Enter the number of elements in the list: "))
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        input_list.append(element)
    return input_list

# Example usage:
my_list = get_list()
print_list(my_list)