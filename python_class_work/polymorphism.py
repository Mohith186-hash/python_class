'''class normalUser:
    def playvideo(self,name):
        print(f"\n{name} is playing vedio with :\n1.Normal Quality\n2.Ads Run\n3.No Background play\n4.Limited videos download\n5.Music with ads")
    def likes(self):
        pass
    def comments(self):
        pass
    def share(self):
        pass
    def share(title):
        pass
    def share(description):
        pass
    def share(subsribe):
        pass

class premiumUser(normalUser):
    def playvideo(self,name):
        print(f"\n{name} is playing vedio with :\n1.High Quality\n2.Ads Free\n3.Background play\n4.Download Anything\n5.Exclusive Music")
        
dinesh = normalUser()
sanjay = premiumUser()
dinesh.playvideo("Dinesh")
sanjay.playvideo("Sanjay")'''

#method overriding
'''class normalUser:
    def playvideo(self,name):
        print(f"\n{name} is playing vedio with :\n1.Normal Quality\n2.Ads Run\n3.No Background play\n4.Limited videos download\n5.Music with ads")
class premiumUser(normalUser):
    def playvideo(self,name):
        print(f"\n{name} is playing vedio with :\n1.High Quality\n2.Ads Free\n3.Background play\n4.Download Anything\n5.Exclusive Music")
def play_video(user,username):
    user.playvideo(username)

dinesh=normalUser()
sanjay=premiumUser()
mohith=normalUser()
tarak=premiumUser()
gopal=premiumUser()
arun=normalUser()

play_video(dinesh,"dinesh")
play_video(sanjay,"sanjay")
play_video(mohith,"mohith")
play_video(tarak,"tarak")
play_video(gopal,"gopal")
play_video(arun,"arun")'''

#operator overriding

class number:
    def __init__(self,n):
        self.n=n 
    def __add__(self,other):
        return self.n+other.n
    def __sub__(self,other):
        return self.n-other.n
    def __mul__(self,other):
        return self.n * other.n
    def __str__(self):
        return f"{self.n}"
    def __lt__(self,other):
        return self.n<other.n
    def __gt__(self,other):
        return self.n>other.n
    def __eq__(self,other):
        return self.n == other.n
number1 = number(10)
number2 = number(20)
print(number1+number2)
print(number1-number2)
print(number1*number2)
print(number1)
print(number1<number2)
print(number1>number2)
print(number1)