#Create a Student class with a list of marks. Add a method to return average and pass/fail.
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def grade(self):
        self.avg = sum(self.marks) / len(self.marks)
        if self.avg > 35:
            print(f"{self.name} \n results avg :{self.avg} ,pass")
        else:
            print(f"{self.name} \n results avg :{self.avg} ,fail")
s1 = Student("mohith",[56,86,86])
s2 = Student("Ram",[25,35,22])
s1.grade()
s2.grade()