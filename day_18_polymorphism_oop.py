# ======================================POLYMORPHISM IN OOP======================================


# ==OPERATOR OVERLOADING==
#when the same operator is allowed to have different meaning according to the context
class Complex:
    def __init__(self, real , imag):
        self.real = real
        self.imag = imag
    def showNumber(self):
        print(self.real, "i +", self.imag, "j")

    def add(self, objectNo1):
        newReal = self.real + objectNo1.real
        newImag = self.imag + objectNo1.imag
        return Complex(newReal, newImag)

    def __add__(self, objectNo1):                        #not this is dunder functions addition
        newReal = self.real + objectNo1.real
        newImag = self.imag + objectNo1.imag
        return Complex(newReal, newImag)

    def __sub__(self, objectNo1):                        #not this is dunder functions substraction
        newReal = self.real - objectNo1.real
        newImag = self.imag - objectNo1.imag
        return Complex(newReal, newImag)

num1 = Complex(3,5)
num1.showNumber()
num2 = Complex(4,4)
num2.showNumber()

# num3 = num1.add(num2)
# num3.showNumber()


# add = num1 + num2         #with the help of dunder function this become possible
# add.showNumber()

sub = num1 - num2             #substraction dunder
sub.showNumber()
