# Create simple Bank Management System in Python using OOP.

class BankAccount:
    def __init__(self, name, account_number, password, balance=0.00):
        self.name = name
        self.account_number = account_number
        self.__password = password   # private
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount, password):
        if password != self.__password:
            print("Incorrect password! Withdrawal denied.")
            return
        
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self, password):
        if password == self.__password:
            print(f"Your balance is: ₹{self.balance}")
        else:
            print("Incorrect password!")

    def display_info(self):
        print("------ Account Information -------")
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("---------------------------------")


# Create a new bank account
def create_account():
    name = input("Enter your name: ")
    acc_no = input("Enter account number: ")
    password = input("Set your password: ")
    balance = int(input("Enter initial deposit: "))
    return BankAccount(name, acc_no, password, balance)


# Main menu-driven program
def bank_menu(account):
    while True:
        print("\n---- Bank Menu ----")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Account Info")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amt = int(input("Enter amount to deposit: "))
            account.deposit(amt)

        elif choice == "2":
            amt = int(input("Enter amount to withdraw: "))
            pwd = input("Enter password: ")
            account.withdraw(amt, pwd)

        elif choice == "3":
            pwd = input("Enter password to view balance: ")
            account.check_balance(pwd)

        elif choice == "4":
            account.display_info()

        elif choice == "5":
            print("Thank you for banking with us!")
            break

        else:
            print("Invalid choice! Try again.")


account = create_account()
bank_menu(account)