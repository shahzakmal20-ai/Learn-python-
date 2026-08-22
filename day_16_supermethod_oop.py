# ==============================================SUPER METHOD IN PYTHON==============================================
# super method is used to access the method of parent class

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("The car is started successfully..")


class Hundayi(Car):
    def __init__(self,brand,type):
        super().__init__(type) #here we set the parent class attribute using super keyword
        self.brand = brand
        super().start()  #here start the car


car = Hundayi("Suzzuki", "Electric")

print("The Type of car: ", car.type)
print("Brand of car: ", car.brand)