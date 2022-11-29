from logic.player_logic import player_logic
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
                pass
            elif command == '2':
                pass
           
