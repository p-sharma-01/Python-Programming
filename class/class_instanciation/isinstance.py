class CustomNumber:
  def __init__(self,value):
    self.value=value
  def __add__(self,other):
    if isinstance(other,CustomNumber): # isinstance always take two arguments 1. object and 2. is class ... it refines  whether it is the instance of class
      return CustomNumber(self.value + other.value)
    else:
      return CustomNumber(self.value + other)
  def __mul__(self,other):
    if isinstance(other,CustomNumber):
      return CustomNumber(self.value * other.value)
    elif isinstance(other,str):
       return 'It is not possible.'
    else:
      return CustomNumber(self.value*other)
  def __div__(self,other):
    if isinstance(other,CustomNumber):
      return CustomNumber(self.value / other.value)
    elif isinstance(other,str):
      return 'It is not possible.'
    else:
      return CustomNumber(self.value/other)
  def __sub__(self,other):
    if isinstance(other,CustomNumber):
      return CustomNumber(self.value - other.value)
    elif isinstance(other,str):
      return 'It is not possible.'
    else:
      return CustomNumber(self.value-other)
  def __floordiv__(self,other):
    if isinstance(other,CustomNumber):
      return CustomNumber(self.value // other.value)
    elif isinstance(other,str):
      return 'It is not possible.'
    else:
      return CustomNumber(self.value//other)

  def __str__(self):
    return f'{self.value}' # here the c become the main object which store the dtata
# main
a=CustomNumber(12)
b=CustomNumber(2)
c=a+b
d=a*b
e=a//b
f=a/b
g=a-b
print(c)
print(d)
print(e)
print(f)
print(g)



# a=3+4.5
# print(isinstance(a,float)) # True