import ATMlogic as atm

atm.Welcome()
acc=input("Enter the account number: ")
pin=int(input("Enter the pin: "))


while True:
    if atm.login(acc,pin):
        atm.menu()
        op=int(input("Select the option: "))
        if op==0:
            print("Thankyou")
            break
        elif op==1:
            atm.check_balance()
        elif op==2:
            atm.deposit()
        elif op==3:
            atm.withdraw()
        elif op==4:
            atm.view_transaction()
    else:
        break