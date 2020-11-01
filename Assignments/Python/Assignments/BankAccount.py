
class BankAccount :
    def __init__(self, int_rate,balance=0):
        self.int_rate= int_rate
        self.balance = balance

    def deposit (self, amount):
        self.balance += amount
        return self

    def withdraw (self, amount):
        if (amount <self.balance):
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.withdraw(5)
        return self

    def display_account_info(self):
        print('Balance is:', self.balance)
        return self

    def yield_interest(self):
        if (self.balance>0):
            self.balance *= self.balance
            return self
        



user2 = BankAccount(0.01)
user1 = BankAccount(0.01, 200)

user2.deposit(50).deposit(2000).deposit(
    150).withdraw(400).display_account_info()

user1.deposit(5070).deposit(150).withdraw(
    50).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()





        


