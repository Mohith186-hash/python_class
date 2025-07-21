data={
    'prshanth@gmail.com':'123@',
    'dinesh@gmail.com':'789!',
    'sanjay@gmail.com':'456',
    }
email,pwd=input("enter the email and pwd: ").split()
if data.get(email)==pwd:
    print('login successful')
else:
    print('invalid login')

#enter the email and pwd: prshanth@gmail.com 123@
#login successful
''' by using data(email) we will get error
if the data has not present on it so us (.get)'''

items=["idly,samosa,oil,bag"]
stocks=["20,30,10,0"]
data=input("enter the item name: ")
