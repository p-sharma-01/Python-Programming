class Convertor:
    def __init__(self,temperature):
        self.temperature=temperature
    def c_to_f(self):
        print(f"The {self.temperature} in Fahrenheit is {(9/5)*self.temperature+32}.")
    def f_to_c(self):
        print(f"The {self.temperature} in Celsius is {(self.temperature-32)*5/9}.")
    def c_to_k(self):
        print(f"The {self.temperature} in Kelvin is {273.15+self.temperature}")
    def k_to_c(self):
        print(f"The {self.temperature} in Celsius is {self.temperature-273.15}.")
    def f_to_k(self):
        print(f"The {self.temperature} in Kelvin is {((self.temperature-32)*5/9)+273.15}.")
    def k_to_f(self):
        print(f"The {self.temperature} in Fahrenheit is {((9/5)*(self.temperature-273.15))+32}.")
n,temp=map(str,input("Enter the temperature with its specifications seperated by space : ").split())
conv=Convertor(int(n))
if temp=="C":
    conv.c_to_f()
    conv.c_to_k()
elif temp=="K":
    conv.k_to_c()
    conv.k_to_f()
elif temp=="F":
    conv.f_to_c()
    conv.f_to_k()
else:
    print("Wrong Input")

