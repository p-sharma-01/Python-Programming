class Engine:
    def start(self):
        raise NotImplementedError

class ElectricCar(Engine):
    def start(self):
        return "Starting electric motor"
    
    def charge(self):
        return "Charging battery"

class CombustionCar(Engine):
    def start(self):
        return "Starting gasoline engine"
    
    def refuel(self):
        return "Refueling tank"

class HybridCar(ElectricCar, CombustionCar):  # Fix inheritance
    pass

# Test Input
prius = HybridCar()
print(prius.start())  # "Starting electric motor"
print(prius.refuel())  # "Refueling tank"