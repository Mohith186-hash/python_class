class Bank:
    def __init__(self):
        self.name="xyz"
        self.balance=0
    @property
    def noresbalance(self):
        return self._balance
    
    @noresbalance.setter
    def noresbalance(self,amount):
        self._balance+=amount
b=Bank()

print(b.noresbalance)
b.noresbalance=3000
print(b.noresbalance)

print(b.name)
b.name="abc"
print(b.name)
