
roll_nos=[]
class Student:
    def __init__(self):
        self.l=[]
        pass
    def new_student(self, name,roll_no, marks):
        p=[name,roll_no,marks]
        self.l.append(p)
        print("New Student Data Added Suucessfully")
    def display_a_student(self,roll_no):
        for i in self.l:
            if roll_no in i:
                print(f"Name : {i[0]:>15}")
                print(f"Roll Number : {i[1]:>15}")
                print(f"Marks : {i[2]:>15}")
        else:
            print("No Student found by this Roll Number.")
    def display_all(self):
        j=1
        for i in self.l:
            print(f"{j}. Name: {i[0]}  Roll_no: {i[1]}  Marks: {i[2]}")
            j+=1
    def Exit(self):
        print("You Successfully Exited. Thanks for Using.")
student=Student()
print("Welcome to Student Management System.")
s=True
while s:
    n=input("Which Functionality You Wants to use [Add,Display,Search,Exit] : ")
    if n=="Add":
        name=input("Enter Student Name : ")
        roll_no=int(input("Enter Roll_No :"))
        marks=int(input("Enter marks of student :"))
        if roll_no in roll_nos:
            print("Roll Number already Exists.")
        else:
            student.new_student(name,roll_no,marks)
            roll_nos.append(roll_no)
    elif n=="Display":
        student.display_all()
    elif n=="Search":
        roll=int(input("Provide roll number to fetch Student Details :"))
        if roll not in roll_nos:
            print("No Student found by this Roll Number.")
        else:
            student.display_a_student(roll)
    elif n=="Exit":
        student.Exit()
        s=False





