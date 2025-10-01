# Create a Car class with method to update and show odometer after driving.
class Car():
    def __init__(self,car):
        self.car = car
        self.km = 0
    def odometer(self,km):
        self.km += km
        print(f"{self.km} is travelled")
    def display(self):
        print(f"{self.car} is travelled {self.km}")
obj = Car("Toyota")
obj.odometer(45)
obj.odometer(100)
obj.display()
