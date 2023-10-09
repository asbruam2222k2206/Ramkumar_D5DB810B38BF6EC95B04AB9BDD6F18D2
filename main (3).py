class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

# Create an instance of BankAccount
account = BankAccount()

# Test deposit functionality
print(account.deposit(100))  # Deposited $100. New balance: $100

# Test withdrawal functionality
print(account.withdraw(50))   # Withdrew $50. New balance: $50
print(account.withdraw(75))   # Invalid withdrawal amount or insufficient funds.