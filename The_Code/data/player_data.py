import csv
from model.player import Player

class PlayerData:
    def __init__(self):
        self.file_name = 'files/players.csv'

    def create_player(self, player):
        with open(self.file_name, 'a', newline='', encoding = 'utf-8') as csvfiles:
            fieldnames = ['name', 'id', 'address', 'gsm', 'phone', 'email', 'role', 'team']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'name': player.name, 'id': player.id, 'address': player.address, 'gsm': player.gsm, 'phone': player.phone, 'email': player.email, 'role': player.role, 'team': player.team})

    def read_all_players(self):
        return_list = []
        with open(self.file_name, newline='', encoding = 'utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                return_list.append(Player(row['name'], row['id'], row['address'], row['gsm'], row['phone'], row['email'], row['role'], row['team']))
        return return_list
