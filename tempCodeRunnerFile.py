
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
