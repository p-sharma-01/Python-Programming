class BankAccount:
    def __init__(self, initial_balance):
        self.initial_balance=initial_balance
    
    def deposit(self, amount):
        self.initial_balance+=amount
    
    def withdraw(self, amount):
        self.initial_balance-=amount
    
    # Implement this
    def get_balance(self):
        return self.initial_balance

# Test Input
acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.get_balance())  # Expected Output: 120