data = {
    100:{"pin":123,"current_balance":5000,"history":[]},
    200:{"pin":123,"current_balance":6000,"history":[]},
    300:{"pin":123,"current_balance":4500,"history":[]}
}
print("Welcome to ATM")
acc=int(input("enter the account number: "))
pin=int(input("enter the pin: "))
if acc in data and data[acc]["pin"]==pin:
    print("login succesfull")
    while True:
        print('''\n\nATM MENU
          1.Check Balance
          2.Deposit
          3.Withdrawl
          4.History
          5.Exit''')
        op=int(input("Select the option: "))

        if op==1:
            print(f"Current Balance : ₹{data[acc]['current_balance']}")
        if op==2:
            amount=int(input("Enter amount to deposit : "))
            data[acc]["current_balance"]+=amount
            data[acc]["history"].append(f"Deposited ₹{amount}")
            print(f"succesfully deposited ₹{amount}")
        if op==3:
            amount=int(input("Enter the amout: "))
            if data[acc]["current_balance"]>=amount:
                data[acc]["current_balance"]-=amount
                data[acc]["history"].append(f"withdraw ₹{amount}")
                print(f"succesfully withdraw ₹ {amount}")
            else:
                print("insufficent amount")
        if op==4:
            print("Trasition History")
            for i in data[acc]["history"]:
                print(f"-{i}")
        if op==5:
            break


else:
    print("invalid login")
    
