from abc import ABC, abstractmethod

class Upload(ABC):
    @abstractmethod
    def compress(self):
        pass
class Image(Upload):
    def compress(self):
        print("Image is compressed to 2MB")
class Reel(Upload):
    def compress(self):
        print("Reel is compressed to 3MB")
r = Reel ()
i = Image()

r.compress()
i.compress()


###
from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass
class FoodOrder(Order):
    def process_order(self):
        print("Processing Food Order: Check chef availability, estimate time")

class GroceryOrder(Order):
    def process_order(self):
        print("Processing Grocery Order: Check inventory per item")

class MedicineOrder(Order):
    def process_order(self):
        print("Processing medicine Order: Validate prescription, assign secure medicine" )

class CloudKitchenOrder(Order):
    def process_order(self):
        print("Processing Tiffin Subscription: Schedule weekly deliveries")

class PetSuppliesOrder(Order):
    def process_order(self):
        print("Processing Pet Supplies Order: Check pet product categories ")

class MeatOrder(Order):
    def process_order(self):
        print("Processing Meat/Sea food order: confirm freshness, assign chilled")

class CakeOrder(Order):
    def process_order(self):
        print("Processing Cake Order: Custom baking, time-sensitive packaging.")

class PartyOrder(Order):
    def process_order(self):
        print("Processing Party Order: Bulk cooking, team coordination, special order")

class JuiceOrder(Order):
    def process_order(self):
        print("Processing Fresh Juice Order: Immediate prep, cold packaging.")

def handle_order(order:Order):
    order.process_order()

orders = [
    FoodOrder(),
    GroceryOrder(),
    MedicineOrder(),
    CloudKitchenOrder(),
    PetSuppliesOrder(),
    MeatOrder(),
    CakeOrder(),
    PartyOrder(),
    JuiceOrder(),
]

for order in orders:
    handle_order(order)


###

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def make_payment(self,amount):
        pass
class CreditCardPayment(Payment):
    def make_payment(self,amount):
        print(f"Paid ${amount} using Credit Card.")
    
class PayPalPayment(Payment):
    def make_payment(self,amount):
        print(f"Paid ${amount} via Paypal.")

def process_payment(payment, amount):
    payment.make_payment(amount)

process_payment(CreditCardPayment(), 100)
process_payment(PayPalPayment(),200)
