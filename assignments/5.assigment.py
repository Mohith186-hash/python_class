from abc import ABC, abstractmethod   

class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def get_details(self):
        return f"Name: {self.name}, Phone: {self.phone}"

class Customer(User):
    def __init__(self, name, phone, address):
        super().__init__(name, phone) 
        self.address = address
        self.__orders = [] 

    def place_order(self, restaurant, item):
        if item in restaurant.menu:
            price = restaurant.menu[item]
            self.__orders.append((item, price, restaurant.name))
            print(f"{self.name} ordered {item} from {restaurant.name} (₹{price})")
        else:
            print(f"{item} is not available at {restaurant.name}")

    def show_orders(self):
        print(f"\nOrder history of {self.name}:")
        for order in self.__orders:
            print(f"{order[0]} - ₹{order[1]} from {order[2]}")

    def get_total_bill(self):
        return sum(order[1] for order in self.__orders)

class DeliveryBoy(User):
    def __init__(self, name, phone, vehicle):
        super().__init__(name, phone)
        self.vehicle = vehicle

    def deliver_order(self, order):
        print(f"{self.name} is delivering: {order}")

class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

    def show_menu(self):
        print(f"\nMenu of {self.name}:")
        for item, price in self.menu.items():
            print(f"{item} - ₹{price}")

class Payment(ABC):  
    @abstractmethod
    def pay(self, amount):
        pass

class UpiPayment(Payment):
    def __init__(self):
        self.total_bill = total_bill
        self.paid_amount = 0

    def pay(self, amount):
        self.paid_amount += amount
        remaining = self.total_bill - self.paid_amount
        print(f"Paid ₹{amount} in UPI 💵")
        if remaining > 0:
            print(f"Remaining to pay on delivery: ₹{remaining}")
        else:
            print("Full payment received ✅")

class CashOnDelivery(Payment):
    def __init__(self, total_bill):
        self.total_bill = total_bill
        self.paid_amount = 0

    def pay(self, amount):
        self.paid_amount += amount
        remaining = self.total_bill - self.paid_amount
        print(f"Paid ₹{amount} in Cash 💵")
        if remaining > 0:
            print(f"Remaining to pay on delivery: ₹{remaining}")
        else:
            print("Full payment received ✅")

if __name__ == "__main__":
    
    rest1 = Restaurant("Spicy Biryani House", {"Biryani": 200, "Pizza": 300, "Burger": 150})
    rest1.show_menu()

    c1 = Customer("Mohith", "9876543210", "Hyderabad")
    c1.place_order(rest1, "Biryani")
    c1.place_order(rest1, "Pizza")

    d1 = DeliveryBoy("Rajesh", "9998887776", "Bike")
    d1.deliver_order("Biryani from Spicy Biryani House")

    total_bill = c1.get_total_bill()
    print(f"\nTotal Bill: ₹{total_bill}")

    print("\n--- UPI Payment ---")
    upi_payment = UpiPayment()
    upi_payment.pay(200) 
    upi_payment.pay(300) 
    
    c1.show_orders()