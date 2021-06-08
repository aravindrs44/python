class User:
    bank_name = "First National Dojo"

    def __init__(self, name, email_address, account_name):
        self.name = name
        self.email_address = email_address
        self.account_name = BankAccount.account_name
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def display_user_balance(self):
        print(f"{self.name}: {self.account.balance}")

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    # def transfer_money(self, other_user, amount):
    #     self.account_balance -= amount
    #     other_user.account_balance += amount
    #     return self, other_user


class BankAccount:
    bank_name = "Bank of India"

    def __init__(self, int_rate = 0.02, balance = 0):
        self.int_rate = int_rate
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


    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def all_accounts_info(cls):
        print(cls.bank_name)

aravind = User("Aravind Sripada", "sentyss44@gmail.com")

aravind.display_user_balance()
aravind.make_deposit(300).display_user_balance()