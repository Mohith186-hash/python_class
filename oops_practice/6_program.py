class movie:
    def __init__(self,title,rating):
        self.title = title
        self.rating = rating
    def child(self):
        if self.rating<= 13:
            print(f"{self.title} can watch anyone")
        else:
            print(f"{self.title} only watch by elders")

t1 = movie("OG",11)
t1.child()
t2= movie("svsc",14)
t2.child()