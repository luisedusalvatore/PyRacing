import pygame
import random
from configuracoes import *
from funcoes import *
from janela import *
from game_screen import *

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PyRacing')

state = INIT
cor = None
while state != QUIT:
    if state == INIT:
        state, cor = start(window) 
    elif state == GAME and cor is not None:  
        state = game_screen(window, cor)
    else:
        state = game_over(window)

pygame.quit()