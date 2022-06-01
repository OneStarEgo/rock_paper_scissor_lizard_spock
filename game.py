
class Game:
    
    def __init__(self):
        print()

    def play_game(self):
       self.display_greeting()
       self.rules()
       self.player_headcount()
    
    def display_greeting(self):
        print("Welcome player and/or players to Rock, Paper, Scissors, Lizard, Spock!")
    
    def rules(self):
        print("""The rules are as follows:
        Rock crushes Scissors
        Scissors cut Paper
        Paper covers Rock
        Rock crushes Lizard
        Lizard poisons Spock
        Spock smashes Scissors
        Scissors decapitate Lizard
        Lizard eats Paper
        Paper disproves Spock
        Spock vaporizes Rock

        two players
        Best two out of three wins!""")

    def player_headcount(self):
        player_input = input("How many Players? 1 or 2 ")
        

