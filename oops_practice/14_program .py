class Employee:
    def __init__(self, name):
        self.name = name
    def show_role(self):
        print("General employee")


class Manager(Employee):
    def show_role(self):
        print("Manager with team responsibilities")

mgr = Employee("Ravi")
mgr.show_role()