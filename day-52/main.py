# 52.Class BankAccount with deposit and withdraw methods.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawn: ${amount}. Remaining Balance: ${self.balance}")

    def __str__(self):
        return f"BankAccount of {self.owner} - Balance: ${self.balance}"


# Example usage
account = BankAccount("Alice", 100)
print(account)

account.deposit(50)
account.withdraw(30)
account.withdraw(150)
