class Payment:
    def pay(self, amount):
        raise NotImplementedError("Child classes must implement pay()")


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount:.2f} using Credit Card")


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount:.2f} using UPI")


class NetBanking(Payment):
    def pay(self, amount):
        print(f"Paid {amount:.2f} using Net Banking")


if __name__ == "__main__":
    payments = [CreditCard(), UPI(), NetBanking()]
    for payment in payments:
        payment.pay(500)
