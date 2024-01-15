Bank Account Management System This is a simple Bank Account Management System implemented in Python. It allows users to create a bank account, perform deposits, withdrawals, and check the current balance. The system is designed with two classes: BankAccount and Menu.
BankAccount Class The BankAccount class represents a bank account and includes the following methods:
init(self, account_holder_name, account_number, balance=0): Initializes a new bank account with the given account holder name, account number, and an optional initial balance (default is 0).
deposit(self, amount): Deposits a specified amount into the account. Prints the new balance after the deposit.
withdraw(self, amount): Withdraws a specified amount from the account if sufficient funds are available. Prints the new balance after the withdrawal.
display_balance(self): Displays the account holder's name, account number, and current balance.
Menu Class The Menu class is a simple class that provides a static method show_menu() to display the available options for the user.
How to Use Run the program and provide the required information such as account holder name, account number, and initial balance.
Choose from the following options:
Deposit: Deposit a specific amount into the account. Withdraw: Withdraw a specific amount from the account. Display Current Balance: View the current balance and account information. Exit: Terminate the program. Follow the on-screen instructions to interact with the bank account.
Sample Usage Enter account holder name: Nanjundi Enter account number: 987654321 Enter initial balance: 1000
Options:
1.	Deposit
2.	Withdraw
3.	Display Current Balance
4.	Exit
Enter your choice (1-4): 1 Enter the deposit amount: 500 Deposited ₹500. New balance: ₹1500
Options:
1.	Deposit
2.	Withdraw
3.	Display Current Balance
4.	Exit
Enter your choice (1-4): 3 Account Holder: Nanjundi Account Number: 987654321 Current Balance: ₹1500
Options:
1.	Deposit
2.	Withdraw
3.	Display Current Balance
4.	Exit
Enter your choice (1-4): 4 Exiting program.Good bye!


