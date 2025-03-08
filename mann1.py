class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0):
        # Private attributes
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__balance = balance

    # Getter and Setter for account_number
    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    # Getter and Setter for account_holder_name
    def get_account_holder_name(self):
        return self.__account_holder_name

    def set_account_holder_name(self, account_holder_name):
        self.__account_holder_name = account_holder_name

    # Getter and Setter for balance
    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative.")

    # Method to deposit money
    def deposit(self, amount):
        if amoun
        else:
            print("Insufficient funds. Withdrawal denied.")

# Testing the class
account = BankAccount("12345678", "John Doe", 1000)

# Accessing and modifying private attributes using getter and setter methods
print(account.get_account_number())
account.set_account_number("87654321")
print(account.get_account_number())

# Performing transactions
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)  # Should fail due to insufficient funds
t > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be greater than zero.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")