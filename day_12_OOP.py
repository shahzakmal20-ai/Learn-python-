# ============================CLASS & OBJECTS IN PYTHON==============================


class Student:
     name = "John Doe"
     age = 23
     rollNo = 234
     marks = 98.4


# st = Student()
# print(st.name , st.age ,st.marks, st.marks)




# ======================Constuctor in python=================



class Car:
    company = "G-Wagon"
    def __init__(self):
          print("This is my default constuctor... ")

    
    def __init__(self, car_color , mod):  #parameterize constuctor
         self.color = car_color
         print("The car color come in constuctor from where object is called: ", self.color)
         print("The car model is: ", mod)
         print("company: ",self.company)

         



obj = Car("yellow", 2026)
obj1 = Car("Brown", 2000)


