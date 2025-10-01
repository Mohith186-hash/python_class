# Account and SavingsAccount
class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited {amount}")
        print(f"{amount} has been deposited. Current balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.history.append(f"Withdrew {amount}")
            print(f"{amount} has been withdrawn. Current balance: {self.balance}")
        else:
            print("Insufficient balance")

    def acc_history(self):
        print(f"Transaction history for {self.name}:")
        for h in self.history:
            print("-", h)


class SavingsAccount(Account):
    def __init__(self, name, balance=0, minimum_balance=1000):
        super().__init__(name, balance)   # ✅ fixed
        self.minimum_balance = minimum_balance

    def acc_minimum_balance(self, amount):
        if self.balance - amount >= self.minimum_balance:
            self.balance -= amount
            self.history.append(f"Withdrew {amount} (min balance rule)")
            print(f"{amount} withdrawn successfully. Current balance: {self.balance}")
        else:
            print(f"Cannot withdraw {amount}. Minimum balance of {self.minimum_balance} must be maintained.")


# ✅ Example usage
obj1 = SavingsAccount("Tarak", 4000, 2000)
obj1.deposit(2000)
obj1.withdraw(3000)
obj1.withdraw(1500)
obj1.withdraw(2000)
obj1.acc_history()
obj1.acc_minimum_balance(1000)

