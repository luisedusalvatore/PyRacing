import pygame
from configuracoes import *
import os
from classes import *
from assets import load_assets
from funcoes import *

def game_screen(window):
    assets = load_assets()
    clock = pygame.time.Clock()
    background = assets[fundo]
    all_sprites = pygame.sprite.Group()
    all_enemies = pygame.sprite.Group()
    groups = {}
    groups['all_enemies'] = all_enemies
    groups['all_sprites'] = all_sprites
    groups['background'] = background

    player = Piloto(groups, assets)
    all_sprites.add(player)

    for i in range(3):
        inimigo = Carro(assets)
        all_sprites.add(inimigo)  # Add individual enemy to all_sprites
        all_enemies.add(inimigo)


    DONE = 0
    PLAYING = 1
    EXPLODING = 2
    state = PLAYING

    keysdown = {}
    score = 0
    lives = 4

    while state != DONE:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            if state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        player.speedx -= 12
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player.speedx += 12
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        player.speedx += 12
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player.speedx -= 12

        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, all_enemies, False, pygame.sprite.collide_mask)  # Changed to False to keep enemies
            if hits:
                lives -= 1
                explosao = Explosion(player.rect.center, assets)
                all_sprites.add(explosao)
                player.kill()
                state = EXPLODING
                keysdown = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosao) + 400

        elif state == EXPLODING:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                if lives == 0:
                    state = DONE
                else:
                    state = PLAYING
                    player = Piloto(groups, assets)  # Complete respawn
                    all_sprites.add(player)
                    player.speedx = 0  # Reset speed to ensure control


        window.fill(BLACK)
        window.blit(groups['background'], (0, 0))
        all_sprites.draw(window)
        all_sprites.update()
        pygame.display.update()