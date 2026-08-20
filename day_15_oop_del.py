# ===================================Del keyword in python========================================


class Student:
    def __init__(self,name):
        self.name = name


s1 = Student("Ali Hassan")
# print(s1.name)
# print(s1)
# del s1
# print(s1) #s1 object is not existed its deleted from the memory




# ===========================Public or private attribute in the class============================================
#in python add 2 underscore at start of name to make private the attribute
class Account:
    def __init__(self, accountNo, password):
        self.accountNo = accountNo
        self.__password = password #passwor is private here


acc = Account("adcfg23445", "2354")
# print(acc.accountNo)
# print(acc.__password) #not able to access thsi password here



class Person:
    __name = "Ali Khan"                #private attribute

    def __hello(self):           #private method not accessible out of class
        print("Hello ALi")

    def welcom(self):
        self.__hello()

p = Person()
print(p.welcom()) # this well call the private hello
# print(p.__name)
# p.__hello