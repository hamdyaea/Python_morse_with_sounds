import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame                                                                                                                                                                                                                                 
import time                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                              
class MorsePlayer:                                                                                                                                                                                                                            
    def __init__(self, text, morse_code):                                                                                                                                                                                                     
        self.text = text                                                                                                                                                                                                                      
        self.morse_code = morse_code                                                                                                                                                                                                          
        pygame.mixer.init()                                                                                                                                                                                                                   
                                                                                                                                                                                                                                              
    def translate_to_morse(self):                                                                                                                                                                                                             
        return ' '.join([self.morse_code.get(c.upper(), '') for c in self.text])                                                                                                                                                              
                                                                                                                                                                                                                                              
    def play_sound(self, letter):                                                                                                                                                                                                             
        sound_path = f'sounds/{letter}.wav'                                                                                                                                                                                                   
        sound = pygame.mixer.Sound(sound_path)                                                                                                                                                                                                
        sound.play()                                                                                                                                                                                                                          
        time.sleep(sound.get_length())                                                                                                                                                                                                        
                                                                                                                                                                                                                                              
    def play_morse(self):                                                                                                                                                                                                                     
        morse_text = self.translate_to_morse()                                                                                                                                                                                                
        print(f"Text in morse : {morse_text}")                                                                                                                                                                                                
        for letter in morse_text:                                                                                                                                                                                                             
            if letter == '.':                                                                                                                                                                                                                 
                self.play_sound('dot')                                                                                                                                                                                                        
            elif letter == '-':                                                                                                                                                                                                               
                self.play_sound('dash')                                                                                                                                                                                                       
            elif letter == ' ':                                                                                                                                                                                                               
                time.sleep(0.5)
            else:
                print(f"{letter} is not a letter in morse and will be ignored.")
        pygame.mixer.pause()

