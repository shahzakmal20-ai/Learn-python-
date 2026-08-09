# =====================================Open With Statement========================
# USING 'with' statement to open a file is a good practice because it automatically takes care of closing the file after the block of code is executed, even if an error occurs. This helps to prevent resource leaks and ensures that the file is properly closed.





with open("demo.txt", "r") as f:  # Open the file in read mode using 'with' statement
    data = f.read()  # Read the entire content of the file
    print(data)  # Print the content of the file
    print(type(data))  # Print the type of the data read from the file
    print(f.name)  # Get the name of the file





# =====================write mode with 'with' statement========================

with open("open_with_file.txt", "w") as file_write:  # Open the file in write mode using 'with' statement
    file_write.write("This is a new data by write mode.\n")  # Write a new line to the file
    file_write.write("This is another line that will be written to the file.\n")  # Write another new line to the file

# ===end===