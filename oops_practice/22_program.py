class Printer:
    def print_file(self):
        print("Generic printing")

class InkjetPrinter(Printer):
    def print_file(self):
        print("Inkjet printing...")
class LaserPrinter(Printer):
    def print_file(self):
        print("Laser printing...")
obj1 = LaserPrinter()
obj1.print_file()
obj2 = InkjetPrinter()
obj2.print_file()
#start_printing(LaserPrinter())
