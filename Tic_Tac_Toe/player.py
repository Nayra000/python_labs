class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""
    
    def choose_name(self):
        while True:
            name = input("Enter your name: ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Please use only letters.")

    def choose_symbol(self):
        while True:
            symbol = input("Choose your symbol (X or O): ")
            if symbol.upper() in ["X", "O"]:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol. Please choose X or O.")