# ===============================Encapsulation in python ======================================

# means data and method work as a single unit

class Employee:
   name = ""
   salary = 0
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
   def details(self):
      print(f"Employee name is: {self.name} and his salary is: {self.salary}")



emp = Employee("Haider Ali", 50000)

emp.details()