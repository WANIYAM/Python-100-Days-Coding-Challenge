# 59.Demonstrate encapsulation with private attributes.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute
        self.__balance = balance    # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

    def get_balance(self):
        return self.__balance
account = BankAccount("Alice", 1000)

account.deposit(500)
account.withdraw(200)

# Accessing public attribute
print("Owner:", account.owner)

# Trying to access private attribute directly (will cause an error)
# print(account.__balance)  ❌

# Accessing private attribute using a method (correct way)
print("Balance:", account.get_balance())
