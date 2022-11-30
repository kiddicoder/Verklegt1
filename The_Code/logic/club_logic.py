from data.club_data import ClubData
from model.club import Club

class PlayerLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_club(self, club):
        self.club_logic.create_club(club)

    def list_all_clubs(self):
        return self.club_logic.list_all_clubs()
