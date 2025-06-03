
class Employee:
    def __init__(self,name,id,dept,salary):
        self.name=name
        self.id=id
        self.dept=dept
        self.salary=salary
        self.data=[]
    def display(self):
        k=f'''Name      :{self.name}
ID        :{self.id}
Department:{self.dept}
Salary    :{self.salary}\n'''
        
        print(k)
    def update(self,name=None,dept=None,salary=None):
        if name:
            self.name=name
        if dept:
            self.dept=dept
        if salary:
            self.salary=salary
    def increment(self,inc):
        self.salary+=self.salary*(inc/100)
        print("Increment Successfully Registered\n")
class Employee_management():
    def __init__(self):
        self.reg={}

    def add_employee(self,id):
        if id in self.reg:
            print("Data is already with same id.\n")
        else:
            self.reg[id]=Employee(emp_name,e_id,e_dept,e_salary)
            print(f'Data with Employee ID {id} successfully Created.\n')
    def display_all_employee(self):
        for i in self.reg:
            self.reg[i].display()
    def incraese_by_id(self,id,perc):
        self.reg[id].increment(perc)
    def delete(self,id):
        self.reg.pop(id)
        print("Data deleted successfully\n")
system=Employee_management()
while True:
    print("Welcome To GLA UNIVERSITY \n")
    print('''
1.Add EMployee
2. Update Employee INfo
3.Display All employess
4.Delete employee by id
5.Salary increment by id
6.Exit''')
    choice=int(input("Enter the choice [1-6] :"))   
    if choice==1:
        emp_name=input("Enter name :")
        e_id=int(input("Enter Id: "))
        e_dept=input("Enter department :")
        e_salary=int(input("enter salary :"))
        employee=Employee(emp_name,e_id,e_dept,e_salary)
        system.add_employee(e_id)
    elif choice==2:
        emp_name=input("Enter New Name :")
        e_dept=input("Enter New Department :")
        e_salary=int(input("Enter New Salary :"))
        system.update(emp_name,e_dept,e_salary)
    elif choice==3:
        system.display_all_employee()
    elif choice==4:
        e_id=int(input("Enter id you wants to delete :"))
        system.delete(e_id)
    elif choice==5:
        e_id=int(input("Enter id you wants to increase the salary :"))
        p=int(input("Enter percentage :"))
        system.incraese_by_id(e_id,p)
    elif choice==6:
        print("You exit successfully ")
        break