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
    explosion_tick = 0
    explosion_duration = 850  # 50ms * 9 frames + 400ms buffer

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
            hits = pygame.sprite.spritecollide(player, all_enemies, True, pygame.sprite.collide_mask)
            for hit in hits:
                explosao = Explosion(hit.rect.center, assets)
                all_sprites.add(explosao)
                lives -= 1
                new_inimigo = Carro(assets)
                all_sprites.add(new_inimigo)
                all_enemies.add(new_inimigo)
                if lives == 0:
                    explosao = Explosion(player.rect.center, assets)
                    all_sprites.add(explosao)
                    player.kill()
                    state = EXPLODING
                    explosion_tick = pygame.time.get_ticks()

        elif state == EXPLODING:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                state = DONE



        window.fill(BLACK)
        window.blit(groups['background'], (0, 0))
        all_sprites.draw(window)
        all_sprites.update()
        pygame.display.update()