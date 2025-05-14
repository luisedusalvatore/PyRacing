import pygame
from configuracoes import *
import os
from classes import *
from assets import *
def game_screen(window):
    # Relógio do sistema
    clock = pygame.time.Clock()
    background = assets[fundo]
    player = Piloto (groups, assets)

    state = True
    while state != False:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = False
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(background, (0, 0))
        # atualiza a tela
        pygame.display.update()