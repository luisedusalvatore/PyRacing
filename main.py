"""Arquivo principal do jogo PyRacing.

Este arquivo inicializa o Pygame, configura a janela do jogo e gerencia o fluxo
entre as telas de início, jogo e game over.
"""

import pygame
import random
from configuracoes import *
from funcoes import *
from janela import *
from assets import *
from game_screen import *

# Inicializa o Pygame e o mixer de áudio
pygame.init()
pygame.mixer.init()

# Cria a janela principal do jogo com as dimensões definidas
window = pygame.display.set_mode((WIDTH, HEIGHT))
# Define o título da janela
pygame.display.set_caption('PyRacing')

# Estado inicial do jogo
state = INIT
# Cor do carro do jogador (inicialmente None)
cor = None
# Pontuação do jogador (inicialmente 0)
score = 0

# Loop principal do jogo
while state != QUIT:
    # Tela inicial
    if state == INIT:
        state, cor = start(window)
    # Tela do jogo
    elif state == GAME and cor is not None:
        state, score = game_screen(window, cor)
    # Tela de game over
    elif state == GAME_OVER:
        state = game_over(window, score)

# Finaliza o Pygame
pygame.quit()