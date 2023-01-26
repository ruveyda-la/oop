class BankAccount:
    int_rate = 0.05
    balance = 0
    all_accounts=[]

    def __init__ (self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)


    def deposit(self,amount):
        self.balance += amount
        return self 

    def withdraw (self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print ("insufficient funds:Charging a $5 fee")
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

    @classmethod
    def BankAccountInfo (cls):
        for account in cls.all_accounts:
            print(f"{account.int_rate},{account.balance}") 
        


account1 = BankAccount(0.1,500)
account2 = BankAccount(0.5,200)

account1.deposit(50).deposit(25).deposit(25).withdraw(200).yield_interest().display_account_info()
account2.deposit(100).deposit(50).withdraw(100).withdraw(150).withdraw(100).withdraw(1000).yield_interest().display_account_info()


BankAccount.BankAccountInfo()

