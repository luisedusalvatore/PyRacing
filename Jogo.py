import pygame
import random
from configuracoes import *
from funcoes import *
from janela import *
from game_screen import *

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PyRacing')

state = INIT 
while state != QUIT:
    if state == INIT:
        state = start(window)
    elif state == GAME:
        state = game_screen(window)
    else:
        state = game_over(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados    