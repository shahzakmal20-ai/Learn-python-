# ==============================================CLASS METHOD============================================
#class method is bound to the class and recieve the class as a implicit first argument. 
#STATIC METHOD cannot access or modify class state and generally for utility/

class Student:
    name = "Jason Roy"

    def change_name(self,name):
        self.name = name               #thsi create new object level attribute it cannot update class attribute name
        # self.__class__.name = name
        # Student.name = name


student = Student()
# student.change_name("Jos Buttler")

# print(student.name)
# print(Student.name)


# ===============================CLASS METHOD=================================

class Person:
    name = "John Doe"
    @classmethod       #decorator
    def changeName(cls,name):
        cls.name = name


p = Person()
p.changeName("Jason")
# print(p.name)





# ==========================PROPERTY DECORATOR=====================================

class Student2:
    def __init__(self, phy, chem, math):
         self.phy = phy
         self.chem = chem
         self.math = math

    @property
    def percentage(self):
        return str((self.math + self.chem + self.phy)/3)+ "%"

st = Student2(87,65,78)
print(st.percentage)
st.phy = 67
print(st.percentage)
