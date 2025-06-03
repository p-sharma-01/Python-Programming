# using instace we can't change the data in the class variable

class student:
    count=0 # class variable , common for all instances
    def __init__(self,name,rollno):
        self.name=name # Instance variable
        self.rollno=rollno
    def __str__(self):
        return'I always executed when call .'# always acts as finally statement in the exception handling.
    def __repr__(self):
        return ' i print the representation.'
    
obj1=student('ravi',34)
obj2=student('shyam',45)
obj1.count=10
obj1.count+=2 # it only change the count value for a instance
print(obj2.count)
print(obj1.count) # only change value for first instance i.e 2
print(obj2.count)# still have the value 0
print(student.count)# 0
# print(obj1,obj2)
# obj1# representation
# obj2# representation
# print(obj1.name)
# print(obj2.name)
# student.count+=2# it will update the count value that is 2
