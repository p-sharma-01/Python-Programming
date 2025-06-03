class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def addition(self):
        return f"Addition of {self.num1} and {self.num2} is {self.num1+self.num2}."
    def substraction(self):
        return f"Substraction of {self.num2} from {self.num1} is {self.num1-self.num2}."
    def multiplication(self):
        return f"Multiplication of {self.num1} and {self.num2} is {self.num1*self.num2}."
    def division(self):
        if self.num2==0:
            return "Zero Division Error Occur. Please take correct Inputs!!!"
        else:
            return f"Division of {self.num1} by {self.num2} is {self.num1/self.num2}"
    def exit(self):
        return "Thanks for using our calculator ... Come Again next time."
condition=True
while True:
    n1,n2=map(int,input("enter two numbers seperated by spaces : ").split())
    p=input("Which operation you wants to perform [addition,substraction,multiplication,division,exit]: ")
    calc=Calculator(n1,n2)
    if p=="addition":
        print(calc.addition())
    if p=="substraction":
        print(calc.substraction())
    if p=="multiplication":
        print(calc.multiplication())
    if p=="division":
        print(calc.division())
    if p=="exit":
        print(calc.exit())
        condition=False
