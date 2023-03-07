from model.morse_code import MorsePlayer
from view.user_input import UserInput


class MorseController:
    def __init__(self):
        self.user_input = UserInput()
        self.morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}
        self.morse_player = MorsePlayer('', self.morse_code)

    def run(self):
        text = self.user_input.get_input()
        self.morse_player.text = text
        self.morse_player.play_morse()

