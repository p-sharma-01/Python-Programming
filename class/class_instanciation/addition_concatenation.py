class sample:
  def __add__(self,other): # merge operator
    print('Thid is the concatenation.')
obj1=sample()
obj2=sample()
c=obj1+obj2

a=10
b=20
print(a.__add__(b))

