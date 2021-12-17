import sys
sys.path.insert(0,'\\data\\')
from data.game import Game, Initiating
import pygame

g = Game()
i = Initiating()
i.initiate()

#background_song = pygame.mixer.music.load('aud/soundtrack.mp3')
pygame.mixer.Channel(0).play(pygame.mixer.Sound('data/aud/soundtrack.mp3'), loops=-1)

pygame.mixer.Channel(0).set_volume(0.04)

while g.running:
    g.current_menu.display_m()
    g.game_loop()



