class Employee:
    def __init__(self, name, salary):
        self.__name=name
        self.__salary=salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name=name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary=salary
ob=Employee('ankush',1098767890987656789098765678)
print(ob._Employee__name)
# Example usage:
# Read input and manipulate employee details
