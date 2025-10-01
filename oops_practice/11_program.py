# Vehicle and Car Inheritance
class Vechile():
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print(f"{self.brand} is started")
class Car(Vechile):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model
    def display(self):
        print(f"{self.brand} , {self.model}")
car1 = Car("Toyota", "Camry")
car1.start()
car1.display()
