'''#Create a Book class with title, author, and price. Add a method to display all book details.
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
b2.text()'''

'''text="hello world"
reversed_each=" ".join(word[::-1] for word in text.split())
print(reversed_each)
print(text[::-1])'''

'''n = 5
for i in range(n):
    for j in range(i,n):
        print('',end = ' ')
    for j in range (i+1):
        print(j+1,end = ' ')
    print()'''

'''n = 5
for i in range(1,n+1):
    for j in range(i,n):
        print(" ", end=" ")

    for j in range(i+1):
        if j == 0 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

'''n = 5
for i in range(1, n+1):
    # leading spaces
    for j in range(i, n):
        print("  ", end="")   # 2 spaces for alignment

    # stars and hollow spaces
    for j in range(i+1):
        if j == 0 or j == i or i == n:  # first, last, or bottom row
            print("* ", end="")         # star with space
        else:
            print("  ", end="")         # hollow space (2 spaces)
    print()'''

n = 5
for i in range(1, n+1):
    # leading spaces
    for j in range(i, n):
        print("  ", end="")   # 2 spaces

    # stars and hollow spaces
    for j in range(i+1):
        if j == 0 or j == i or i == n:   # edges or last row
            print("* ", end="")          # 2 chars wide
        else:
            print("  ", end="")          # 2 chars wide for hollow
    print()




