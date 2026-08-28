# QUESTION 1

class Circle:
    def __init__(self,raduis):
        self.raduis = raduis

    def Area(self):
        return (22/7) * self.raduis * self.raduis

    def Perimeter(self):
        return (22/7) * 2 * self.raduis


cir = Circle(21)
# print("Area of circle: ", cir.Area())
# print("Perimeter of circle: ", cir.Perimeter())





# QUESTION 2

class Employee:
    def __init__(self, role, dep,salary):
        self.role = role
        self.dep = dep
        self.salary = salary

    def showDetails(self):
        print("Role of Employee: " ,self.role)
        print("Dep. of Employee: " ,self.dep)
        print("Salary of Employee: " ,self.salary)


class Engineer(Employee):
    def __init__(self, name , age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT",600000)


# e1 = Employee("accountant", "Finance", 440000)   
# e1.showDetails()

eng1  = Engineer("John", 23)
eng1.showDetails()