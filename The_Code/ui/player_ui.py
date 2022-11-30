from logic.player_logic import PlayerLogic
from model.player import Player 
from ui.input_validators import *

class Player_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def output_menu(self):
        print('Player menu')
        print('1) Create player')
        print('2) List all players')
        print('b) to go back')

    def input_prompt(self):
        while True:
            self.output_menu()
            command = input('Enter your command: ')
            command = command.lower()
            if command == 'b':
                print('going back')
                return 'b'
            elif command == '1':
                p = Player()
                while True:
                    p.name = input('Enter the name of the player: ')
                    p.player_id = input('Enter the player id: ')
                    p.address = input('Enter the address of the player: ')
                    p.email = input('Enter the email of the player: ')
                    p.gsm = input('Enter the mobile phone number of the player: ')
                    p.phone = input('Enter the phone number of the player: ')
                    p.role = input('Enter the role of the player: ')
                    p.team = input('Enter the name of the players team: ')
            elif command == '2':
                result = self.logic_wrapper.list_all_players()
                for elem in result:
                    print(f'name: {elem.name}, id: {elem.player_id}, address: {elem.address}, email: {elem.email}, mobile phone: {elem.gsm}, phone: {elem.phone}, role: {elem.role}, team: {elem.team}')
            else: 
                print('invalid input, try again')
           
