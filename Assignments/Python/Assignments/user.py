class User :
    def __init__ (self, name, email, account_balance):
        self.name= name
        self.email= email
        self.account_balance= account_balance

    def make_deposit(self, amount):	
        self.account_balance += amount
        return self
    def make_withdrawal (self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance (self):
        print('User name:', self.name, "user's Balance:", self.account_balance)
        return self
    
    def transfer_money(self, other_user, amount):
        other_user = amount
        self.account_balance -= amount
        print("Other user tranfer money:",other_user,'User name:',self.name ,'Remaning balance:', self.account_balance)
        return self




user1= User('John','JOhn@gmail.com',100)
user2= User('Ralph', 'Ralph"gmail.com', 900)
user3= User('Pual', 'Paul@gmail.com', 4000)
user4=User('Hassan', 'Hassan@gmail.com',9300)
user5=User('Sara', 'Sara@gmail.com', 800)

user2.make_withdrawal(700).make_deposit(1000).display_user_balance()
user1.make_deposit(3000).transfer_money(100,100).display_user_balance()
user5.make_deposit(1010).make_deposit(200).make_deposit(300).make_withdrawal(50).transfer_money(150,150)





        


