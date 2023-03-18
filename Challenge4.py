class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
        
class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate
acc = Account("Ashish", 5000)
print(acc.title)       # Output: Ashish
print(acc.balance)     # Output: 5000

sacc = SavingsAccount("Ashish", 5000, 5)
print(sacc.title)          # Output: Ashish
print(sacc.balance)        # Output: 5000
print(sacc.interestRate)   # Output: 5
