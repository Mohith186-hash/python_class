'''class Shape:
    def __init__(self, color):
        self.color = color
    def display_color(self):
        print(f"Color: {self.color}")

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width
    def area(self):
        A = self.length * self.width
        print("Area: ",A)

rect = Rectangle("Blue", 4, 5)
rect.display_color()
rect.area()'''

class Shape:
    def __init__(self,length,breadth,colour):
        self.length = length
        self.breadth = breadth
        self.colour = colour
class Reactangle(Shape):
    def __init__(self,length,breadth,colour,):
        super().__init__(length,breadth,colour)
    def rect_area(self):
        A = self.length * self.breadth
        print(f"Area : ",A)
obj1 = Reactangle(4,5,"blue")
obj1.rect_area()

        