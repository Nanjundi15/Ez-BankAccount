class BankAccount:
    def __init__(self,account_holder_name,account_number,initial_balance=0.0):
        self.account_holder_name=account_holder_name
        self.account_number=account_number
        self.balance=initial_balance
        
    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            print(f"Deposit of rs={amount} successful.")
            print(f"New balance: rs={self.balance}")
        else:
            print("invalid deposit amount .please enter a positive value.")
            
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance-=amount
                print(f"withdrawal of rs={amount} successful. ")
                print(f"New balance: rs={self.balance}")
            else:
                print("Insufficient funds. Withdrawl canceled.")
                
        else:
            print(" Invalid Withdrawl amount. Please enter a positive value.")
    
    def display_balance(self):
        print(f"Account holder =={self.account_holder_name}")
        print(f"Account number =={self.account_number}")
        print(f"rs =={self.balance}")
        
if __name__=="__main__":
    name = input("Enter account holder name: ")
    acc_number=input("Enter account number: ")
    initial_balance=float(input("Enter initial balance: "))
    
    account =BankAccount(name,acc_number,initial_balance)
    
    while True:
        print("\n 1.Deposit\n2.Withdraw\n3. Display Balance\n4 . Exit")
        choice =input("Enter youir choice(1/2/3/4): ")
        
        if choice =="1" :
            amount =float(input("Enter the deposit amount:"))
            account.deposit(amount)
            break
        elif choice=="2":
            amount=float(input("Enter the withdrawal amount: "))
            account.withdraw(amount)
            break
        elif choice == '3':
            account.display_balance() 
            break 
        elif choice=="4":
            print("Exiting program.Good bye!")
            break
        else:
            print("Invalid choice. please enter a valid option.")
            exit