from logic.club_logic import ClubLogic
from logic.match_logic import MatchLogic
from logic.player_logic import PlayerLogic
from logic.team_logic import TeamLogic
from logic.tournament_logic import TournamentLogic
from data.data_wrapper import DataWrapper

class LogicWrapper:
    def __init__(self):
        self.data_wrapper = DataWrapper()
        self.club_logic = ClubLogic()
        self.match_logic = MatchLogic()
        self.player_logic = PlayerLogic()
        self.team_logic = TeamLogic()
        self.tournament_logic = TournamentLogic()
    
    def create_player(self, player):
        return self.player_logic.create_player(player)

    def list_all_players(self):
        return self.player_logic.list_all_players()
    
    def create_tournament(self, tournament):
        return self.tournament_logic.create_tournament()
