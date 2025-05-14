import pygame
import random
from configuracoes import *
from funcoes import *
from janela import *

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PyRacing')

state = INIT
while state != QUIT:
    if state == INIT:
        state = janela(window)
    elif state == GAME:
        state = janela(window)
    else:
        state =janela(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados