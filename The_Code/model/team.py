from model.player import Player

class Team():
    def __init__(self, player="", team_name=""): 
        self.player = Player()     
        self.team_name = team_name

    def __str__(self):
        return f"{self.player}, {self.team_name}"
