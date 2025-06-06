class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped...")
    
class ToyotaCar(Car):
    def __init__(self, name,type):
        super().__init__(type) #used to access methods of parent class
        self.name = name

car1 = ToyotaCar("fortuner","diesel")
car2 = ToyotaCar("prius","electric")

print(car1.type)
print(car2.type)


# single inheritance - Base class -> child class
# multilevel inheritance - Base class -> child class -> child class ...
# multiple inheritance - Inherits properties from multiple base classes.