class Bank:
    def __init__(self, n, b, w, d, ph, p):
        self.name = n
        self.balance = b
        self.withdraw = w
        self.deposit = d
        self.phone = ph
        self.pin = p
        
    def account(self):
        print(" ------------------ ACCOUNT DETAILS ------------------ ")
        print("Name:", self.name)
        print("Phone:", self.phone)
        print("Balance: ₹", self.balance)
        print("------------------------")
    
    def change_phone(self, new_phone):
        self.phone = new_phone
        print("Phone number updated successfully!")

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("PIN number updated successfully!")

accounts = []

print("                 -----------WELCOME---------") 
print("                 ---ONLINE BANKING SYSTEM---")
how = int(input("How many accounts you want to add: "))
for i in range(how):
    print(f"\nEnter details for account {i + 1}:")
    n = input("Enter your name: ")
    b = int(input("Enter your current balance: ₹"))
    ph = input("Enter your phone number: ")
    pi = input("Enter your PIN number: ")
    
    acc = Bank(n, b, 0, 0, ph, pi)
    accounts.append(acc)

while True:
    wh = input("What would you like to do\n1.check balance\n2.withdraw money\n3.deposit money\n4.change phone number\n5.change PIN\n6.EXIT\n: ")
    
    if wh == 'check balance' or wh == '1':
        if how > 1:
            ask = input("Name of the account holder you want to check bank balance of: ")
            for acc in accounts:
                if acc.name == ask:
                    acc.account()
                    break
            else:
                print("Account not found ")
        
        else:
            for acc in accounts:
                    acc.account()


    elif wh == 'withdraw money' or wh == '2':
        if how > 1:
            name = input("Enter the account holder's name: ")
            w = int(input("Amount you want to withdraw: "))
            for acc in accounts:
                if acc.name == name:
                    ans = b - w
                print("             AMOUNT TRANSFERRED SUCCESSFULLY")
                print(f"Amount after withdraw: {ans}")
        else:
            w = int(input("Amount you want to withdraw: "))
            ans = b - w
            print("             AMOUNT TRANSFERRED SUCCESSFULLY")
            print(f"Amount after withdraw: {ans}")
            break

    elif wh == 'deposite money' or wh == '3':
        if how > 1:
            name = input("Enter the account holder's name: ")
            j = int(input("Amount you want to deposit: ₹"))
            for acc in accounts:
                if acc.name == name:
                    acc.balance += j
                    print(f"--------------------- AMOUNT AFTER --------------------- DEPOSIT\n{acc.balance}")
        else:
            j = int(input("Amount you want to deposit: ₹"))
            ans = b - j
                    print(f"--------------------- AMOUNT AFTER --------------------- DEPOSIT\n{ans}"  break

    elif wh == 'change phone number' or wh == '4':
        if how > 1:
            name = input("Enter the account holder's name to find your account: ")
            new_phone = input("Enter new phone number: ") 
            for acc in accounts:
                if acc.name == name:
                    acc.change_phone(new_phone)
                    
        else:
            new_phone = input("Enter new phone number: ") 
                acc.change_phone(new_phone)
            break

    elif wh == 'change PIN' or wh == '5':
        name = input("Enter the account holder's name: ")
        new_pin = input("Enter new PIN: ")
        for acc in accounts:
            if acc.name == name:
                acc.change_pin(new_pin)
                break
    
    else:
        print("       EXITING THANKYOU FOR BANKING WITH US")
        exit()
