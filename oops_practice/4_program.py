# Create a BankAccount class with deposit, withdraw, and balance display.
class BankAccount():
    def __init__(self,name,Balance=0):
        self.name = name
        self.Balance = Balance
    def deposit(self,amount):
        self.Balance += amount
        print(f"{amount} has succesfully deposited current balance {self.Balance}")
    def withdraw(self,amount):
        if self.Balance >= amount:
            self.Balance -= amount
            print(f"{amount} is succesfully withdrawn current balance {self.Balance}")
        else:
            print("Insufficent balance")
    def display(self):
        print(f"Account Holder {self.name} current balance is {self.Balance}")
obj = BankAccount("Tarak",5000)
obj.deposit(5000)
obj.withdraw(1000)
obj.display()

