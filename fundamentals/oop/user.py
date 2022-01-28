#creating the user class
from bank_account import BankAccount


class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email  
        self.account = BankAccount(name, int_rate=.1, balance = 200)
#adding the deposit method to the user class
    def make_deposit(self, amount):
        self.account.deposit
        return self
    #adding the check balance method
    def checkBalance(self):
        self.account.display_account_info
        return self
    #adding withdraw method
    def make_withdrawal(self, amount):
        self.account.withdraw
        return self
    #adding the transfer_money method
    def transfer_money(self, user, amount):
        self.account_balance -= amount
        user.account_balance += amount
        print(self.account_balance)
        print(user.account_balance)

#created 3 instances of the user class
user(name="", email="")
don = user(name="", email="")
charles = user(name="", email="")
marge = user(name="", email="")

don.name = "Don"
charles.name = "Charles"
marge.name = "Marge"

#user1 making 3 deposits and 1 withdrawal
don.make_deposit(500).make_deposit(200).make_withdrawal(150)

#user2 making 2 deposits and 2 withdrawals
charles.make_deposit(5000).make_deposit(15000).make_withdrawal(200).make_withdrawal(150)

#user3 making 1 deposit and 3 withdrawals
marge.make_deposit(500000).make_withdrawal(20).make_withdrawal(60).make_withdrawal(10000)

#user 1 transfers money to user3
don.transfer_money(marge, 100)