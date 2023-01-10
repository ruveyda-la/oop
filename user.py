class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print (self.first_name,self.last_name,self.email,self.age,sep='\n')

    def enroll(self):
        if self.is_rewards_member == True:
            print('User already a member.')
            return False
        else:
            self.is_rewards_member = True 
            self.gold_card_points = 200
            return True


    def spend_points(self,amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            return self.gold_card_points
        else:
            print ('User doesnot have enough points.')

id1 = User('Jane','Doe','Janedoe@email.com','32')
id1.display_info()

id2 = User('Jack','Brown','Jackbrown@email.com','45')
id3 = User('Mary','Thomson','Marythomson@email.com','61') 
id1.enroll()
print (id1.spend_points(50))  
id2.enroll()
print (id2.spend_points(80))

id2.display_info()
id3.display_info()
id1.enroll()
id1.spend_points(250)
