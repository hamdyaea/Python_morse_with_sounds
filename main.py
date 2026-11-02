#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Translate text to Morse code, optionally playing local WAV sounds."""
import argparse
from controller.main import MorseController

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", help="Text to translate; prompts if omitted")
    parser.add_argument("--play", action="store_true", help="Play dot and dash WAV sounds")
    args = parser.parse_args()
    controller = MorseController()
    text = args.text if args.text is not None else input("Enter text to translate: ")
    controller.morse_player.text = text
    morse = controller.morse_player.translate_to_morse()
    print(morse)
    if args.play:
        controller.morse_player.play_morse()

if __name__ == "__main__":
    main()
