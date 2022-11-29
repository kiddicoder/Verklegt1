from model.team import Team
from model.player import Player

class Match():
    def __init__(self, home_team="" away_team="", home_player="", away_player="", results="", date_of_match="", new_date_of_match=""):
        self.home_team = Team()
        self.away_team = Team()
        self.home_player = Player()
        self.away_player = Player()
        self.results = self.ResultsOfMatch()
        self.date_of_match = self.DateOfMatch()
        self.new_date_of_match = self.PostponeMatch()
    
    def ResultsOfMatch(self):  #veit ekki hvernig ég á að gera þessi föll
        pass

    def DateOfMatch(self):
        pass

    def PostponeMatch(self):
        pass

    def __str__(self):
        return f"{self.home_team}, {self.away_team}, {self.home_player}, {self.away_player}, {self.results}, {self.date_of_match},{self.new_date_of_match}"
