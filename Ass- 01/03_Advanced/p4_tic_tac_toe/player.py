import random

# Ye Player class ka base class hai, jisse Human aur Computer player inherit karte hain
class Player:
    def __init__(self, letter):
        self.letter = letter  # Har player ka symbol hoga jaise 'X' ya 'O'
    
    def get_move(self , game):
        pass  # Ye method child classes mein define kiya jaayega

# Ye RandomComputerPlayer class hai jo random move choose karta hai
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)  # Parent class ka constructor call kiya gaya
    
    def get_move(self, game):
        square = random.choice(game.available_moves())  # Random move choose karta hai available moves mein se
        return square

# Ye HumanPlayer class hai jahan user se input liya jaata hai
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)  # Parent class ka constructor call kiya gaya
    
    def get_move(self, game):
        valid_square = False  # Jab tak user valid square nahi deta, loop chalta rahega
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')  # User se move input lete hain
            try:
                val = int(square)  # Input ko integer mein convert karte hain
                if val not in game.available_moves():  # Agar move available nahi hai toh error raise karte hain
                    raise ValueError
                valid_square = True  # Agar move valid ho toh loop se nikal jaate hain
            except ValueError:
                print('Invalid square. Try again.')  # Agar galat input ho toh error message show karte hain

        return val  # Valid move return karte hain
