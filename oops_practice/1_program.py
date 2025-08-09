class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author = author
        self.price = price
    def text(self):
        print("Book Details".center(50,'*'))
        print(f"{self.title},{self.author},{self.price}")
b1 = Book("jncdsjffnsj","dnjsbd",5654650)
b1.text()
b2 = Book("nshdhds","jdsbfb",55615)
b2.text()
