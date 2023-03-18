class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
    
    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.balance * self.interestRate) / 100


demo1 = SavingsAccount("Ashish", 2000, 5)   # initializing a SavingsAccount object
demo1.deposit(500)                         # depositing 500 in the account
print(demo1.getBalance())                  # output: 2500
demo1.withdrawal(500)                      # withdrawing 500 from the account
print(demo1.getBalance())                  # output: 2000
print(demo1.interestAmount())              # output: 100.0 (as interestRate is 5% of 2000)
