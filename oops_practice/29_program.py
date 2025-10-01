class Transport:
    def book(self):
        pass

class Bus(Transport):
    def book(self):
        print("Bus ticket booked")

class Flight(Transport):
    def book(self):
        print("Flight ticket booked")

obj1 = Flight()
obj2 = Bus()
obj1.book()
obj2.book()