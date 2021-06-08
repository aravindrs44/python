class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account_balance = 0

    def display_user_balance(self):
        print(f"{self.name}: {self.account_balance}")

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self, other_user

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
aravind = User("Aravind Sripada", "aravindrs@hotmail.com")
guido.make_deposit(50).make_deposit(100).make_deposit(150).make_withdrawal(200).display_user_balance()
monty.make_deposit(100000).make_deposit(10).make_withdrawal(3000000).display_user_balance()
aravind.make_deposit(50).make_withdrawal(10).make_withdrawal(10).make_withdrawal(10).display_user_balance()
aravind.transfer_money(monty, 10)
monty.display_user_balance()
aravind.display_user_balance()