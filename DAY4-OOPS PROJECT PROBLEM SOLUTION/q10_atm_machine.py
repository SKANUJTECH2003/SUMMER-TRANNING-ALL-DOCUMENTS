class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def verify_pin(self, entered_pin):
        return entered_pin == self.__pin

    def deposit(self, entered_pin, amount):
        if self.verify_pin(entered_pin):
            if amount > 0:
                self.__balance += amount
                print(f"Deposit successful. New balance: {self.__balance}")
            else:
                print("Deposit amount must be positive.")
        else:
            print("PIN verification failed.")

    def withdraw(self, entered_pin, amount):
        if self.verify_pin(entered_pin):
            if amount <= 0:
                print("Withdrawal amount must be positive.")
            elif amount > self.__balance:
                print("Insufficient balance.")
            else:
                self.__balance -= amount
                print(f"Withdrawal successful. Remaining balance: {self.__balance}")
        else:
            print("PIN verification failed.")

    def change_pin(self, entered_pin, new_pin):
        if self.verify_pin(entered_pin):
            self.__pin = new_pin
            print("PIN changed successfully.")
        else:
            print("PIN verification failed.")

    def display_balance(self, entered_pin):
        if self.verify_pin(entered_pin):
            print(f"Current balance: {self.__balance}")
        else:
            print("PIN verification failed.")


if __name__ == "__main__":
    atm = ATM(1234, 5000)
    atm.display_balance(1234)
    atm.deposit(1234, 1000)
    atm.withdraw(1234, 3000)
    atm.change_pin(1234, 4321)
    atm.display_balance(4321)
