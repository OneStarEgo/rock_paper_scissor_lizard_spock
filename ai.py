from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__("WALL-E")

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
        print(f'{self.name} has picked {self.chosen_gesture}')