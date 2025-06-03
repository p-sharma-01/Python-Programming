class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I make some sound"

class Dog(Animal):  # Inheriting from Animal
    def speak(self):
        return "Bark!"

dog = Dog("Buddy")
print(dog.name)     # Output: Buddy
print(dog.speak())  # Output: Bark!
