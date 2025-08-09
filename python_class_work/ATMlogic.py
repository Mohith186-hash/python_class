data={
    '1234':{'balance':45678,'pin':123,'history':[]},
    '5678':{'balance':56789,'pin':123,'history':[]},
    '5690':{'balance':98798,'pin':123,'history':[]},
    '5612':{'balance':45678,'pin':12,'history':[]},
    '2345':{'balance':19876,'pin':123,'history':[]},
    '6789':{'balance':1999999998,'pin':123,'history':[]},
    }

acc_num=None
login_status=False

def Welcome():
    print('Welcome to the ATM'.center(40,'-'))

def menu():
    print('1.Check Balance')
    print('2.Deposit')
    print('3.Withdraw')
    print('4.View Transation')
    print('0.Exit')

def login(acc,pin):
    if acc in data:
        if data[acc]['pin']==pin:
            global acc_num
            global login_status
            acc_num=acc
            login_status=True
            print("Login Successful")
            return True
        else:
            print("Invalid Pin")
            return False
    else:
        print("Invalid Account Number")
        return False

def check_balance():
    if login_status and acc_num:
        print(f"Current Balance: {data[acc_num]['balance']}")        
    else:
        print("Login Again")

def deposit():
    if login_status and acc_num:
        amount=int(input("Enter the amount to deposit: "))
        data[acc_num]['balance']+=amount
        data[acc_num]['history'].append(f'Deposited :${amount}')
        print(f"{amount} is successfully deposit")
    else:
        print("Login Again")


def withdraw():
    if login_status and acc_num:
        amount=int(input("Enter the amount to withdraw: "))
        if amount<=data[acc_num]['balance']:
            data[acc_num]['balance']-=amount
            data[acc_num]['history'].append(f'Withdraw :${amount}')
            print(f"{amount} is successfully Withdraw")
        else:
            print("Insufficient Balance")
    else:
        print("Login Again")


def view_transaction():
    if login_status and acc_num:
        if data[acc_num]['history']:
            print("\nTransactions: ")
            for i in data[acc_num]['history']:
                print(i)
            print("End of the Transaction\n")
        else:
            print("No Tranasactions")
    else:
        print("Login Again")