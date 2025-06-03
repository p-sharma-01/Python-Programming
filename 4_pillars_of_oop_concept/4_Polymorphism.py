class Bird:
    def fly(self):
        return "Some birds can fly"

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies fast"

class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly"

birds = [Sparrow(), Penguin()]

for bird in birds:
    print(bird.fly())  # Different behavior for each subclass

# overloading
class car:
    def __init__(self,*args):
        self.x=args[0]
        self.y=args[1]