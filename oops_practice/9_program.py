# Create an item that tracks and updates quantity.
class Store():
    def __init__(self,name):
        self.name = name
        self.quantity = 0
    def add(self,quantity):
        self.quantity += quantity
    def display(self):
        print(f"{self.name} of having quantity {self.quantity}")
obj = Store("Pen")
obj.add(63)
obj.add(37)
obj.display()

