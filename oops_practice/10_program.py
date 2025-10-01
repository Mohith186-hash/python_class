#Track order status updates.
class App():
    def __init__(self,order_name):
        self.order_name = order_name
        self.location = None
    def up_location(self,location):
        self.location = location
    def display(self):
        print(f"{self.order_name} is on location {self.location}")

obj = App("Biryani")
obj.up_location("Kukatpally")
obj.display()
