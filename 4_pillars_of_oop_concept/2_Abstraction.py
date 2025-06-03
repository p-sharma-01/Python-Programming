from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method (must be implemented in subclass)

class Dog(Animal):
    def make_sound(self):
        return "Bark!"

dog = Dog()
print(dog.make_sound())  # Output: Bark!
