print("This is time for solving  excercise")

students = {
   "Ararve" : [85, 90, 78],
   "Priya" : [72,68,75],
   "Rohan" : [45,52,48],
   "Sneha" : [95,92,98],
   "Manish" : [60,65,70]
}

# print("student name is: ",students["Ararve"])
# print("student name is: ",students["Priya"])
# print("student name is: ",students["Rohan"])
# print("student name is: ",students["Sneha"])
# print("student name is: ",students["Manish"])

print("\n\n\n\nExplore students using loop\n\n")
for student in students:
   average = 0
   status = ""
   for marks in students[student]:
      average = average + marks /3
      if average >= 80 and average < 101:
         status = "Topper"
      elif average >=60 and average < 80:
         status = "pass"
      elif average < 60 and average > 0:
         status = "needs improvement"
      else:
         status = "invalid"
        
   print(f"{student}: {average} :: {status}") 