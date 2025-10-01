'''class Student:
    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks
    def get__name(self):
        return self.__name
    def set__name(self,name):
        self.__name = name
    def get__marks(self):
        return self.__marks
    def set__marks(self,marks):
        if marks > 0:
            self.__marks = marks
            print(f"{marks} has got")
        else:
            print(f"Invalid marks entered")
obj = Student("Alice",45)
print(obj.get__name())
print(obj.get__marks())
obj2 = Student("Bob",38)
print(obj2.get__name())
print(obj2.get__marks())'''

class Bank():
    def __init__(self,__name,__balance=100):
        self.__name = __name
        self.__balance = __balance
        self.__history = []
    def get__name(self):
        return self.__name
    def set__name(self,name):
        self.__name = name
    def get__balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount > 0:
            self.__deposit += amount
            self.__history.append(f"deposited: {amount}")
            print(f"{amount} Successfully deposited")
        else:
            print(f"Invalid amount Entered")
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__history.append (f"withdraw: {amount}")
            print(f"{amount} is succesfully withdraw")
        else:
            print(f"Insufficent balance")
    def get__history():
        return self.__history
    def set__history(self):
        print(f"transcitional history for{self.__name}")
        for item in self.__history:
            print(item)
acc = Bank()
acc = "Mohith",500
acc.deposit(1000)
acc.withdraw(100)
acc.withdraw(400)
print(acc.get_balance())
acc.history()


        




