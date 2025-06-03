class Account:
  def __init__(self,number,holder_name):
    self.__number=number # private
    self._holder_name=holder_name
  def get_number(self): # Getter methord
    return self.__number
g=Account(24343,'Mukul')
# print(g.__number) attributeError
k=g.get_number()
print(k)

# public private protected