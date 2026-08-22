# ===========================================INHERITANCE IN PYTHON======================================================
# when one class derived the properties or methods of other class

class Car:                            #single inheritance
    color = "black"
    @staticmethod
    def start():
        print("Car is started.....!")

    @staticmethod
    def stop():
        print("car is stoped .....")


class ToyataCar(Car):
    def __init__(self, name):
        self.name = name




c1 = ToyataCar("Honda civic")
c2 = ToyataCar("Alto")

# print(c1.name , c1.color)
# print(c1.start())

# print(c2.name,c1.color)
# print(c2.stop())

# =====================================Multi level inheritance===================================================

class College:
    name = "Punjab College"
    @staticmethod
    def welcome():
        print("Welcome to Punjab College....")

class Teacher(College):
    def __init__(self, resigination):
        self.resigination = resigination


class Student(Teacher):
    def __init__(self, studentClass):
        self.studentClass = studentClass

student = Student("11 th standard")

# print("College name is: ", student.name)
# print("Mail from college: ", student.welcome())
# print("Class of student: ", student.studentClass)



# ==========================================Multiple Inheritance=================================================

class A:
    varA = "this is class A"

class B: 
    varB = "This is class B.."

class C(A,B):
    varC = "This is class C .."


c = C()
print(c.varA)
print(c.varB)
print(c.varC)