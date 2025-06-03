class student:
  count=0
  __section="EB" # access specifier 
  def methord1(self):
    return 'methord1'
  def _methord2(self):
    return 'methord1'
  
# main
obj1=student()
print(obj1.count)# public
print(obj1._methord2) # protected
print(obj1._student__section) # private
print(obj1.methord1())

