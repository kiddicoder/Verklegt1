from model.player import Player
class Club():
    def __init__(self, club_name="", club_address="", club_phone=0, team=""):
        self.club_name = club_name
        self.club_address = club_address 
        self.club_phone = club_phone
        self.team = Team().id()  

    def __str__(self):
        return f"{self.club_name}, {self.club_address}, {self.club_phone}, {self.team}"
