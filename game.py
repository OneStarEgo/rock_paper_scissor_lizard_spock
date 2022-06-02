from human import Human
from ai import Ai
class Game:
    
    def __init__(self):
        self.player_one = Human()
        self.player_two = None
        print()

    def play_game(self):
       self.display_greeting()
       self.rules()
       self.player_headcount()
       self.play_rounds()
    
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
        player_input = int(input("How many Players? 1 or 2 "))
        if player_input == 1:
            self.player_two = Ai()
        elif player_input == 2:
            self.player_two = Human()

    def play_rounds(self):
        while self.player_one.wins < 2 and self.player_two.wins < 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                print("its a tie! keep playing")
            elif self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Scissors":
                print(f"{self.player_one.name} wins the round {self.player_one.chosen_gesture} crushes {self.player_two.chosen_gesture}")
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Papers":
                print (f"{self.player_one.name} wins the round {self.player_one.chosen_gesture} cuts {self.player_two.chosen_gesture}")
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Rock":
                print(f"{self.player_one.name} wins the round {self.player_one.chosen_gesture} covers {self.player_two.chosen_gesture}")
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Lizard":
                print(f"{self.player_one.name} wins the round {self.player_one.chosen_gesture} crushes {self.player_two.chosen_gesture}")
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Lizard" and self.player_two.chosen_gesture == "Spock":
                print(f"{self.player_one.name} wins the round {self.player_one.chosen_gesture} poisons {self.player_two.chosen_gesture}")
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Spock" and self.player_two.chosen_gesture == "Scissors":
                print(f"{self.player_one.name} wins the round {self.player_one.chosen_gesture} smashes {self.player_two.chosen_gesture}")
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Lizard":
                print(f"{self.player_one.name} wins the round {self.player_one.chosen_gesture} decapitates {self.player_two.chosen_gesture}")
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Lizard" and self.player_two.chosen_gesture == "Paper":
                print(f"{self.player_one.name} wins the round {self.player_one.chosen_gesture} eats {self.player_two.chosen_gesture}")
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Spock":
                print(f"{self.player_one.name} wins the round {self.player_one.chosen_gesture} disproves {self.player_two.chosen_gesture}")
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Spock" and self.player_two.chosen_gesture == "Rock":
                print(f"{self.player_one.name} wins the round {self.player_one.chosen_gesture} vaporizes {self.player_two.chosen_gesture}")
                self.player_one.wins += 1
            else:
                self.player_two.wins += 1
