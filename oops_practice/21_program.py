class Payment:
    def pay(self, amount):
        pass


class CreditCard(Payment):
    def pay(self, amount):
            print(f"Paid {amount} using credit card.")

class PayPal(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

def checkout(payment_method):
    payment_method.pay(250)

checkout(CreditCard())
checkout(PayPal())