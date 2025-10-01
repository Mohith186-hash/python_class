'''balance = 0
history = []   # To store transaction history

while True:
    print("\n--- Banking System ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Show Transaction History")
    print("5. Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 5:
        print("Exiting...")
        break
    
    if choice == 1:
        amt = float(input("Enter deposit amount: "))
        balance += amt
        history.append(f"Deposited {amt}")
        print("Amount Deposited Successfully!")
        
    elif choice == 2:
        amt = float(input("Enter withdrawal amount: "))
        if amt <= balance:
            balance -= amt
            history.append(f"Withdrew {amt}")
            print("Amount Withdrawn Successfully!")
        else:
            print("Insufficient Balance")
            
    elif choice == 3:
        print("Current Balance =", balance)
        
    elif choice == 4:
        print("\n--- Transaction History ---")
        if not history:
            print("No transactions yet.")
        else:
            for h in history:
                print(h)
                
    else:
        print("Invalid choice")'''

data={
'prasanth@gmail.com':'123@',
'Dinesh@gmail.com':'789',
'Sanjay@gmail.com':'456',
}


email,pwd=input("Enter the email and pwd:").split()
if email in data and pwd in data[email]:
    print('login successful')
print(email,pwd)

