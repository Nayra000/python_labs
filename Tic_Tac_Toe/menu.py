class Menu:
    def display_main_menu(self):
        print("Welcome to Tic-Tac-Toe!")
        print("1. Start Game")
        print("2. Quit Game") 
        return self.validate_input()
    
    def display_endgame_menu(self):
        menu_text ="""
            Game Over!
            1. Play Again
            2. Quit Game
            """
        print(menu_text)
        while True:
            return self.validate_input()

    def validate_input(self):
        while True:
            user_input = input("Enter your choice: ")
            if user_input in ["1", "2"]:
                return user_input
            print("Invalid choice. Please choose 1 or 2.")