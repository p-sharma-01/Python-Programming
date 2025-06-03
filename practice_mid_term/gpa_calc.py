class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
    
    def add_course(self, credit, grade):
        self.courses.append((credit, grade))
    
    # Implement this method
    def calculate_gpa(self):
        # Logic here
        pass

# Test Input
student = Student("Alice")
student.add_course(3, 'A')
student.add_course(4, 'B')
print(f"{student.calculate_gpa():.2f}")  # Expected Output: 3.14