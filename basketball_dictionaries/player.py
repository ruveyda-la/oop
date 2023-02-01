from players import players

tyler={
    "name":"Tyler Jordan",
    "age":35,
    "position":"small forward",
    "team":"Brooklyn Nets"
}

class Player:
    def __init__(self,data):
        self.name=data["name"]
        self.age =data["age"]
        self.position = data["position"]
        self.team= data["team"]
    new_team=[]
    @classmethod
    def get_team(cls,team_list):
    
        for player in team_list:
            cls.new_team.append(cls(player))  
        print (cls.new_team)   
    @staticmethod
    def justprint(player):
        print(f"{player.name}")
# print(dir(Player))
# Player.get_team(players)

# player1=Player(players[0])
# Player.justprint(player1)
# player2=Player(players[1])
# player3=Player(players[2])
# player4=Player(players[3])
# player5=Player(players[4])
# player6=Player(players[5])
# player7=Player(tyler)
# print(player7.name)