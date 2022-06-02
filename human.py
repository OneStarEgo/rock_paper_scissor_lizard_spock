from player import Player

class Human(Player):
    def __init__(self):
        self.user_name = ""
        self.set_user_name()
        super().__init__(self.user_name)

    def choose_gesture(self):
        user_choice = int(input("Press 0 for Rock, Press 1 for Papaer, Press 2 for Scissors, Press 3 for Lizard and 4 for Spock"))
        self.chosen_gesture = self.gestures[user_choice]
        print(f'{self.name} has chosen {self.chosen_gesture}')

    def set_user_name(self):
        self.user_name = input("please enter your name")