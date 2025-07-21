a=1
while a<=10:
    print(a)
    a+=1
'''1
2
3
4
5
6
7
8
9
10'''

email,pwd='xyz@gmail.com','xyz@123'

max_attempt=5
cur_attempt=1

while cur_attempt <= max_attempt:
    e=input("enter the email: ")
    p=input("enter the password: ")
    if e==email  and p==pwd:
        print("login successful")
        break
    else:
        print("invalid email or pwd.try again!!")
    cur_attempt+=1
else:
    print("max attempts are done.Try after 5 min")

'''enter the email: hsukahdha
enter the password: dsuakhduah
invalid email or pwd.try again!!
enter the email: kuuhasduhd
enter the password: bakdhka
invalid email or pwd.try again!!
enter the email: ndisakhd
enter the password: bdksha
invalid email or pwd.try again!!
enter the email: hkdsa
enter the password: dalhdsal
invalid email or pwd.try again!!
enter the email: ldsiahdis
enter the password: dashldja
invalid email or pwd.try again!!
max attempts are done.Try after 5 min'''

'''enter the email: hahdiashd
enter the password: hdakhdkahd
invalid email or pwd.try again!!
enter the email: dskahdu
enter the password: bdasdkhu
invalid email or pwd.try again!!
enter the email: xyz@gmail.com
enter the password: xyz@123
login successful'''

