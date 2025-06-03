
class student:
    count=0
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        student.count+=1
    @classmethod # decorator
    def get_count(cls):
        return f'student count {cls.count}' #student.count


obj1=student('ravi',23)
obj2=student('kanha',10)
print(obj1.get_count()) # value 2
print(obj2.get_count()) #value 2
# we can't update the class variabke by any instance