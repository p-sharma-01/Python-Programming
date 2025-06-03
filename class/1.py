class Perform:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def substraction(self):
        return self.a-self.b
    def multiplication(self):
        return self.a*self.b
calc=Perform(10,20)
calc.a+=10 # the calc and self have the same functonality . THe differnce is just it is inside the class but the calc is outside the class.
p=calc.addition()
print(p)
