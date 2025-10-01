#Create an Employee class with name, base_salary. Add a method calculate_annual_salary.
class employee:
    def __init__(self,name,base_salary):
        self.name = name
        self.base_salary = base_salary
    def annual_salary(self):
        print(f"{self.name} annual amount is {self.base_salary * 12}")
s1 = employee('ram',564646)
s2 = employee('Tarak',1645654)
s1.annual_salary()
s2.annual_salary()