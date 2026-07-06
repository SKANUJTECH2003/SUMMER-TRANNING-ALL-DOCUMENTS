class BankAccount:
    def __init__(self, account_holder_name, account_number, balance=0.0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount:.2f}. Remaining balance: {self.balance:.2f}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance:.2f}")


if __name__ == "__main__":
    account = BankAccount("Riya", "SB1001", 5000)
    account.display_balance()
    account.deposit(1500)
    account.withdraw(3000)
    account.withdraw(10000)
    account.display_balance()
