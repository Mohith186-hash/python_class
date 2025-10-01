# Problem: Create Product class with discount application logic.
class Product():
    def __init__(self,name,price):
        self.name = name
        self. price = price
    def discount(self,percent):
        self.price -= self.price * (percent/100)
    def display(self):
        print(f"{self.name} is price with discount {self.price}")

obj = Product("phone",20000)
obj.discount(10)
obj.display()