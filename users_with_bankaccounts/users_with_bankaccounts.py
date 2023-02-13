class BankAccount:

    def __init__ (self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print (f"User deposit:{amount} and the balance is {self.balance}")
        return self

    def withdraw (self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"User withdraw:{amount} and the balance is {self.balance}")
        else:
            self.balance -= 5
            print (f"insufficient funds:Charging a $5 fee and the balance is{self.balance}")
        return self    

    def display_account_info(self):
        print (f"Balance:${self.balance}")
        return self

    def yield_interest (self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        else:
            print("Insufficient funds")
        return self




class User:
    def __init__(self,name,email,ch_int_rate,sa_int_rate):
        self.name = name
        self.email = email
        self.account = {"checking":BankAccount(ch_int_rate,0),
                        "saving":BankAccount(sa_int_rate,0)}
        

    def make_deposit (self,amount,account_key):
        self.account[account_key].deposit(amount)
        return self

    def make_withdrawal (self,amount,account_key):
        self.account[account_key].withdraw(amount)
        return self    

    def display_user_balance(self,account_key):
        print(f"Current balance:{self.account[account_key].balance}")
        return self
    
    def transfer_money(self,amount,other_user,account_key_self,account_key_other_user):
        if amount <= self.account[account_key_self].balance:
            self.make_withdrawal(amount,account_key_self)
            other_user.make_deposit(amount,account_key_other_user)
        else:
            print("Insufficient funds")   
        return self     



user1 = User('Jane Doe','Janedoe@email.com',0.02,0.05)
user2 = User('Jack Brown','Jackbrown@email.com',0.5,0.03)
# user1.make_deposit(100,"checking").make_withdrawal(50,"checking").display_user_balance("checking")

user1.make_deposit(100,"checking")
user1.transfer_money(30,user2,"checking","checking")
