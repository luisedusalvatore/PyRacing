import pygame
from configuracoes import *
import os
from classes import *
from assets import load_assets
def game_screen(window):
    assets = load_assets()
    # Relógio do sistema
    clock = pygame.time.Clock()
    background = assets[fundo]
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['background'] = background

    #Criando o jogador
    player = Piloto (groups, assets)
    all_sprites.add(player)

    state = True
    while state != False:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = False
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(groups['background'], (0, 0))
        # atualiza a tela
        all_sprites.update()
        pygame.display.update()