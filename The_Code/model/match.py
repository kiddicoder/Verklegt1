from model.team import Team
from model.player import Player

class Match():
    def __init__(self, home_team="" away_team="", home_player="", away_player="", results="", date_of_match="", new_date_of_match=""):
        self.home_team = Team().id()
        self.away_team = Team().id()
        self.home_player = Player().id()
        self.away_player = Player().id()
        self.results = self.ResultsOfMatch()
        self.date_of_match = self.DateOfMatch()
        self.new_date_of_match = self.PostponeMatch()
    

    def __str__(self):
        return f"{self.home_team}, {self.away_team}, {self.home_player}, {self.away_player}, {self.results}, {self.date_of_match},{self.new_date_of_match}"
