# ============================= METHODS IN OOP =============================

class Student:
    college = "Punjab college"
    def __init__(self, name, year, percentage):
        self.name = name
        self.year = year
        self.percentage = percentage

    def greet(self):
        print(f"Hello, my name is {self.name}")


    def get_details(self):
        print(f"I have completed my graduatuion in {self.year}")


    def get_percentage(self):
        return self.percentage



# student1 = Student("Ali", 2023, 88.5)   
# student1.greet()
# student1.get_details()
# print(f"I got {student1.get_percentage()}% in my graduation.")




# =======================================Practice questions========================================


class student2:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    def greet(self):
        print(f"Hello, my name is {self.name}")

    def average_marks(self):
        total = 0
        for mark in self.marks:
            total = total + mark
        average = total / len(self.marks)
        return average

# student1 = student2("Ali", [85, 85, 86, 90, 88])
# student1.greet()
# print(f"Average marks: {student1.average_marks()}")




# ================================Static methods in python========================

class Student3:
    # @staticmethod
    def hello():
        print("Hello! this me static method...")


student3 = Student3()
# student3.hello() #when we call this statis method with the help of object then needs to use decorator...
Student3.hello() # no need of any decorator
