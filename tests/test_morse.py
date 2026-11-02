# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import unittest
from controller.main import MorseController

class MorseTests(unittest.TestCase):
    def test_sos(self):
        controller = MorseController()
        controller.morse_player.text = "SOS"
        self.assertEqual(controller.morse_player.translate_to_morse(), "... --- ...")
    def test_word_separator(self):
        controller = MorseController()
        controller.morse_player.text = "A B"
        self.assertEqual(controller.morse_player.translate_to_morse(), ".- / -...")
    def test_unknown_ignored(self):
        controller = MorseController()
        controller.morse_player.text = "A!"
        self.assertEqual(controller.morse_player.translate_to_morse(), ".-")

if __name__ == "__main__":
    unittest.main()
