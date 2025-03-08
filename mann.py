class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientFundsError("Insufficient funds. Withdrawal denied.")
        self.__balance -= amount
        print(f"Withdrew {amount}. New balance: {self.__balance}")

# Usage
try:
    account = BankAccount("12345678", "John Doe", 1000)
    account.deposit(500)
    account.withdraw(1500)  # Will raise error
except InsufficientFundsError as e:
    print(e)
