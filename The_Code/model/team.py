
class Team():
    def __init__(self, player="", team_name=""): 
        self.player = player     # eða  self.player = Player() og importa player klasa ??? 
        self.team_name = team_name

    def __str__(self):
        return f"{self.player}, {self.team_name}"
