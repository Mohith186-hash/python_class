class Details:
    def __init__(self,name,mail,pwd):
        self.name=name
        self.mail=mail
        self.pwd=pwd

    def getpassword(self):
        return self.__pwd
    def setpassword(self,new_password):
        self._pwd=new_password
sumanth = Details("Sumanth","sumanth@gmail.com","Sumanth@123")

print(sumanth.name)
sumanth.name="Sanjay"
print(sumanth.name)

print(sumanth._mail)
sumanth._mail="Sanjay@gmail.com"
print(sumanth._mail)

print(sumanth.getpassword())
sumanth.setpassword("Sanjay@123")
print(sumanth.getpassword())