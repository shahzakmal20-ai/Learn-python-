# ===============================Abstraction in python =====================================
# hiding the implementation detail of the class and only showing the essential features to the user..



class Car:
    def __int__(self):
        self.key = False
        self.accellrator = False
        self.brk  = False
        self.clutch = False

    def start(self):
        self.keys = True
        self.clutch = True
        self. accellrator = True
        print("The car is started successfully...")

    def stop(self):
        self.keys = False
        self.brk = True
        self.accellrator = False
        self.clutch = True
        print("Your car is stoped")



car = Car()
car.start()
car.stop()