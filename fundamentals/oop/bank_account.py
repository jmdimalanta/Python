class BankAccount:
    def __init__(self, name, int_rate = .1, balance = 200):
        self.name = name
        self.interest = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self
    
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -=amount
            print(self.balance)
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
    
    def display_account_info(self):
        print(self.balance)
        return self
    
    def yield_interest(self):
        if BankAccount.has_interest(self.interest):
            (self.balance * .1)
            print(self.balance)
        else:
            print(self.balance)
            return self

    @staticmethod
    def has_interest(self):
        if self.balance > 0:
            return True
        else:
            return False

BankAccount(name="", int_rate=.1, balance= 200)
Mark = BankAccount(name="")
Neil = BankAccount(name="")

Mark.name = "Mark"
Neil.name = "Neil"

#User 1 making 3 deposits,1 withdrawal and yielding interest
Mark.deposit(500).deposit(150).deposit(1000).withdraw(500).yield_interest

#User 2 making 2 deposits and 4 withdrawals and yielding interest
Neil.deposit(5000).deposit(15000).withdraw(100).withdraw(1000).withdraw(500).withdraw(50).yield_interest
