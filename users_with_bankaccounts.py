class BankAccount:
    int_rate = 0.05
    balance = 0

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
    def __init__(self,name,email,account):
        self.name = name
        self.email = email
        self.account = account 
        

    def make_deposit (self,amount,i):
        self.account[i].deposit(amount)
        return self

    def make_withdrawal (self,amount,i):
        self.account[i].withdraw(amount)
        return self    

    def display_user_balance(self,i):
        print(f"Current balance:{self.account[i].balance}")
        return self
    
    # def transfer_money(self,amount,other_user,i):
    #     self.account[i].make_withdrawal(amount)
    #     self.other_user.account[j].make_deposit(amount)
    #     print(self.account[i].balance)
    #     print(self.other_user.account[0].balance)
    #     return self




user1 = User('Jane Doe','Janedoe@email.com',[BankAccount(int_rate=0.02, balance=0),BankAccount(int_rate=0.05,balance=1000)])
# user2 = User('Jack Brown','Jackbrown@email.com',[BankAccount(int_rate=0.5, balance=500)])
user1.make_deposit(100,1).make_withdrawal(50,1).display_user_balance(1)

# transfer_money(500,user2,1,0)

