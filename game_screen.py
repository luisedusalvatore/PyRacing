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

    game = True
    while game:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game = False
            # Aperta a tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or  event.key == pygame.K_a:
                    player.speedx -= 12
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.speedx += 12
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or  event.key == pygame.K_a:
                    player.speedx += 12
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.speedx -= 12
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(groups['background'], (0, 0))
        # atualiza a tela
        all_sprites.draw(window)
        all_sprites.update()
        pygame.display.update()