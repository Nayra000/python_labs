from board import Board
from player import Player
from menu import Menu
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    def __init__(self):
        self.players =[Player() , Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_index_player = 0
   
    def start_game(self):
        choice = self.menu.display_main_menu()

        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
            
    def setup_players(self):
        for number,player in enumerate(self.players,start=1):
            print(f"Player {number}, Enter your details: ")
            if(number == 2 ):
                player.choose_name()
                player.symbol = "X" if self.players[0].symbol == "O" else "O"
            else:
                player.choose_name()
                player.choose_symbol()
            clear_terminal()
    
    def quit_game(self):
        print("Thank you for playing")
    
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                clear_terminal()
                self.board.display_board()

                if self.check_win():
                    print(f"{self.players[1 - self.current_index_player].name} wins!")
                else:
                    print("It's a draw!")

            
                choice = self.menu.display_endgame_menu()

                if choice == "1":
                    self.restart_game()
                    break  
                else:
                    self.quit_game()
                    break

    
    def play_turn(self):
        clear_terminal()
        player = self.players[self.current_index_player]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True :
            try:
                cell_num = int(input("Enter a cell number: "))
                if 0 <= cell_num<= 9 and self.board.update_board(cell_num ,player.symbol):
                    break 
                else:
                    print("Invalid choice ,Try again !")
            except ValueError:
                    print("You should enter a number between 1 and 9")
        self.current_index_player = 1 - self.current_index_player
   
    def check_win(self):
        win_combinations =[
            [0,1,2] ,[3,4,5] ,[6,7,8]
            ,[0,3,6] ,[1,4,7] ,[2,5,8]
            ,[0,4,8] ,[2,4,6]]
        for combo in win_combinations:
            if(self.board.board[combo[0]] == self.board.board[combo[1]] == 
                self.board.board[combo[2]]):
                    return True
        return False
            
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board) #loop on the fly generator expression
   
    def restart_game(self):
        clear_terminal()
        print("hiiiiiiiiiiiiiiiii")
        self.board.reset_board()
        self.current_index_player = 0
        self.play_game()


            