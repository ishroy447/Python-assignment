from bank_account import BankAccount

def test_bank_account():
    # Create a new account
    account = BankAccount("123456789", "John Doe", 1000)
    
    # Test initial balance
    print("Test 1: Initial Balance")
    print(account.get_balance())
    print("Expected: Current balance: $1000")
    print()
    
    # Test deposit
    print("Test 2: Deposit")
    print(account.deposit(500))
    print("Expected: Deposited $500. New balance: $1500")
    print()
    
    # Test invalid deposit
    print("Test 3: Invalid Deposit")
    print(account.deposit(-100))
    print("Expected: Invalid deposit amount")
    print()
    
    # Test withdraw
    print("Test 4: Withdraw")
    print(account.withdraw(200))
    print("Expected: Withdrawn $200. New balance: $1300")
    print()
    
    # Test invalid withdraw
    print("Test 5: Invalid Withdraw")
    print(account.withdraw(2000))
    print("Expected: Invalid withdrawal amount or insufficient funds")
    print()
    
    # Test transaction history
    print("Test 6: Transaction History")
    print("Transaction History:")
    for transaction in account.get_transaction_history():
        print(transaction)
    print("Expected: Should show deposit and withdrawal transactions")

if __name__ == "__main__":
    test_bank_account() 