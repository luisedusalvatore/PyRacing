"""Arquivo principal do jogo PyRacing.

Este arquivo inicializa o Pygame, configura a janela do jogo e gerencia o fluxo
entre as telas de início, jogo e game over.
"""

import pygame
import random
from configuracoes import *
from funcoes import *
from janela import *
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

# Loop principal do jogo
while state != QUIT:
    # Tela inicial: exibe o menu e permite escolher a cor do carro
    if state == INIT:
        state, cor = start(window)
    # Tela do jogo: executa a lógica principal do jogo
    elif state == GAME and cor is not None:
        state = game_screen(window, cor)
    # Tela de game over: exibe mensagem de fim de jogo
    else:
        state = game_over(window)

# Finaliza o Pygame ao sair do jogo
pygame.quit()

