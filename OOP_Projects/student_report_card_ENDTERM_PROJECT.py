class Person:
    def __init__(self, name):
        self._name = name  # Encapsulation using protected attribute
    
    def get_name(self):
        return self._name

class Student(Person):  # Inheritance
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no
        self.marks = {}
    
    def add_marks(self, subject, marks):
        self.marks[subject] = marks
    
    def calculate_grade(self):
        if not self.marks:
            return "No Marks Available"
        average = sum(self.marks.values()) / len(self.marks)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    
    def generate_report(self):
        report = "\n" + "="*30 + "\n"
        report += f"Student Report Card\n"
        report += "="*30 + "\n"
        report += f"Student Name: {self.get_name()}\n"
        report += f"Roll No: {self.roll_no}\n"
        report += "-"*30 + "\n"
        report += "Subjects & Marks:\n"
        for subject, marks in self.marks.items():
            report += f"{subject}: {marks}\n"
        report += "-"*30 + "\n"
        report += f"Final Grade: {self.calculate_grade()}\n"
        report += "="*30 + "\n"
        return report

# Main program
def main():
    students = []
    
    while True:
        print("\n1. Add Student")
        print("2. Add Marks")
        print("3. Generate Report")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            name = input("Enter student name: ")
            roll_no = input("Enter roll number: ")
            student = Student(name, roll_no)
            students.append(student)
            print("Student added successfully!")
        
        elif choice == '2':
            roll_no = input("Enter roll number: ")
            student = next((s for s in students if s.roll_no == roll_no), None)
            if student:
                subject = input("Enter subject name: ")
                marks = int(input("Enter marks: "))
                student.add_marks(subject, marks)
                print("Marks added successfully!")
            else:
                print("Student not found!")
        
        elif choice == '3':
            roll_no = input("Enter roll number: ")
            student = next((s for s in students if s.roll_no == roll_no), None)
            if student:
                print(student.generate_report())
            else:
                print("Student not found!")
        
        elif choice == '4':
            print("Thanks for using the Report Card Generator.")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()

