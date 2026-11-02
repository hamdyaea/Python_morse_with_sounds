# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Morse translation and optional sound playback."""
from __future__ import annotations
from pathlib import Path
import time

SOUNDS = Path(__file__).resolve().parents[1] / "sounds"

class MorsePlayer:
    def __init__(self, text: str, morse_code: dict[str, str]):
        self.text = text
        self.morse_code = morse_code

    def translate_to_morse(self) -> str:
        words = []
        for word in self.text.upper().split():
            letters = [self.morse_code[c] for c in word if c in self.morse_code]
            if letters:
                words.append(" ".join(letters))
        return " / ".join(words)

    def play_morse(self) -> None:
        import pygame
        pygame.mixer.init()
        try:
            dot = pygame.mixer.Sound(str(SOUNDS / "dot.wav"))
            dash = pygame.mixer.Sound(str(SOUNDS / "dash.wav"))
            morse = self.translate_to_morse()
            print("Text in Morse:", morse)
            for symbol in morse:
                if symbol in ".-":
                    sound = dot if symbol == "." else dash
                    channel = sound.play()
                    if channel is not None:
                        while channel.get_busy():
                            time.sleep(0.01)
                elif symbol == "/":
                    time.sleep(0.5)
                else:
                    time.sleep(0.15)
        finally:
            pygame.mixer.quit()
