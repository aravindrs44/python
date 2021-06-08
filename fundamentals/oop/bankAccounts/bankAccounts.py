class BankAccount:
    def __init__(self, intrate, balance = 0):
        self.intrate = intrate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance += (self.balance*self.intrate)
        return self

aravind = BankAccount(0.01, 100)
amma = BankAccount(.10, 1000000)
aravind.deposit(100).deposit(200).deposit(200).withdraw(400).yield_interest().display_account_info()
amma.deposit(500000).deposit(300000).withdraw(100000).withdraw(100000).withdraw(100000).withdraw(100000).yield_interest().display_account_info()

