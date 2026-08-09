# ===============================================FILE HANDLING========================================================

# READING THE FILE


file = open("demo.txt", "r")
# data = file.read()
data = file.read(10)  # Read the first 10 characters of the file
# print(data) 
# print(type(data)) # Open the file in read mode
# print(file.name)  # Get the name of the file
file.close()  # Close the file after reading




# =====================Reading a file line by line========================


f = open("demo.txt", "r")
line1 = f.readline()  # Read the first line of the file
# print(line1)
line2 = f.readline()  # Read the second line of the file
# print(line2)

f.close()  # Close the file after reading





# ===============================writing to a file========================


# file_write = open("demo.txt", "w")  # Open the file in write mode
# file_write.write("I am writing to the file this will replace the entire content.\n")  # Write a new line to

# file.close()  # Close the file after writing

# if file not exist it will create a new file and write to it. If the file already exists, it will overwrite the existing content with the new content.

file_write = open("writetest.txt", "w")  # Open the file in write mode
file_write.write("This is auto created file i only put name it will create file of this name.\n")  # Write a new line to the file
file_write.close()  # Close the file after writing

# ===============================APPENDING TO A FILE========================

apend_file = open("demo.txt", "a")  # Open the file in append mode
apend_file.write("\nThis line will be appended to the file.\n")  # Append a new line to the file
apend_file.write("This is another line that will be appended to the file.\n")  # Append another new line to the file
apend_file.close()  # Close the file after appending





















# end 