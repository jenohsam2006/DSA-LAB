class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def edit_account(self, new_account_number, new_holder_name):
        self.account_number = new_account_number
        self.holder_name = new_holder_name
        print("Account details updated successfully.")

    def account_details(self):
        print(f"\nAccount Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: ₹{self.balance}")

accounts = []

def find_account(acc_number):
    for account in accounts:
        if account.account_number == acc_number:
            return account
    return None

while True:
    print("\n--- Bank System Menu ---")
    print("1. Create New Account")
    print("2. Account Details")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Edit Account Details")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        acc_num = input("Enter new account number: ")
        holder = input("Enter account holder name: ")
        initial = float(input("Enter initial deposit (₹): "))
        accounts.append(BankAccount(acc_num, holder, initial))
        print("Account created successfully!")

    elif choice in ["2", "3", "4", "5", "6"]:
        acc_num = input("Enter account number: ")
        account = find_account(acc_num)
        if account:
            if choice == "2":
                account.account_details()
            elif choice == "3":
                amount = float(input("Enter deposit amount: ₹"))
                account.deposit(amount)
            elif choice == "4":
                amount = float(input("Enter withdrawal amount: ₹"))
                account.withdraw(amount)
            elif choice == "5":
                account.check_balance()
            elif choice == "6":
                new_acc_num = input("Enter new account number: ")
                new_name = input("Enter new holder name: ")
                account.edit_account(new_acc_num, new_name)
        else:
            print("Account not found.")

    elif choice == "7":
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice. Please try again.")
