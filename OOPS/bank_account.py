class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: +${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")
            return f"Withdrawn ${amount}. New balance: ${self.balance}"
        return "Invalid withdrawal amount or insufficient funds"

    def get_balance(self):
        return f"Current balance: ${self.balance}"

    def get_transaction_history(self):
        return self.transaction_history

# Example usage
if __name__ == "__main__":
    # Create a new bank account
    account = BankAccount("123456789", "John Doe", 1000)
    
    # Perform some transactions
    print(account.deposit(500))
    print(account.withdraw(200))
    print(account.get_balance())
    print("\nTransaction History:")
    for transaction in account.get_transaction_history():
        print(transaction) 