class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    
    # Implement this
    def area(self):
        return 3.14*self.radius**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
    
    # Implement this
    def area(self):
        return self.width*self.length

# Test Input
circle = Circle(7)
print(circle.area())  # Expected Output: ~153.94 (pi*r^2)