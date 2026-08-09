# ======================Practice Question========================



# with open("practice.txt", "w") as file:
#     file.write("Hi everyone!.\n")  # Write a new line to the file
#     file.write("We are learning File I/O.\n Using JavaScript and Python.\n")  # Write another new line to the file
#     file.write("I like programming in Java\n")  # Write another new line to the file



with open("practice.txt", "r") as file:
    data = file.read()  # Read the entire content of the file

data_new = data.replace("Java", "Python")  # Replace "JavaScript" with "Python" in the content
# print(data_new)  # Print the modified content



# ====WRITE NEW CONTENT TO THE FILE========================
with open("practice.txt", "w") as file:
    file.write(data_new)  # Write the modified content back to the file


# =======finding data from the file========================
# with open("practice.txt", "r") as file:
#     data = file.read()  # Read the entire content of the file
#     if "Python" in data:  # Check if "Python" is present in the content
#         print("Yes, 'Python' is present in the file.")  # Print a message if found
#     else:
#         print("No, 'Python' is not present in the file.")  # Print a message if not found


# with open("practice.txt", "r") as file:
#     data = file.read()
#     if (data.find("Python") != -1):  # Check if "Python" is present in the content using find() method
#         print("Yes, 'Python' is present in the file.")  # Print a message if found
#     else:
#         print("No, 'Python' is not present in the file.")  # Print a message if not found



# =======Checking word for line===============================
def check_word_in_line():
    with open("practice.txt", "r") as file:
        word_to_find = "programming"
        line_number = 1  # Line number counter
        data = True
        while data:
            data = file.readline()  # Read one line at a time
            if word_to_find in data:  # Check if the word is present in the line
                print(f"Yes, '{word_to_find}' is present in line {line_number}.")  # Print a message if found
                break  # Exit the loop if found
            line_number += 1  # Increment the line number counter


        return -1


check_word_in_line()  # Call the function to check for the word in the file





















# end