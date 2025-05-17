import pygame
from configuracoes import *
import os
import random
from classes import *
from assets import load_assets
from funcoes import *

def game_screen(window):
    assets = load_assets()
    clock = pygame.time.Clock()
    background = assets[fundo]
    all_sprites = pygame.sprite.Group()
    all_enemies = pygame.sprite.Group()
    all_vidas = pygame.sprite.Group()
    all_faixas = pygame.sprite.Group()

    groups = {}
    groups['all_enemies'] = all_enemies
    groups['all_sprites'] = all_sprites
    groups['all_vidas'] = all_vidas
    groups["all_faixas"] = all_faixas
    groups['background'] = background

    player = Piloto(groups, assets)
    all_sprites.add(player)

    # Initial track sprites
    left = Esquerda(assets)
    right = Direita(assets)
    all_sprites.add(left, right)
    all_faixas.add(left, right)

    DONE = 0
    PLAYING = 1
    EXPLODING = 2
    state = PLAYING

    keysdown = {}
    score = 0
    lives = 4
    max_lives = 8
    explosion_tick = 0
    explosion_duration = 850
    last_vida_spawn = pygame.time.get_ticks()
    vida_spawn_interval = random.randint(10000, 30000)  # 10-30 seconds
    faixa_spawn_interval = 250  # Reverted to 6 seconds to avoid clutter
    last_faixa_spawn = pygame.time.get_ticks()
    last_enemy_spawn = pygame.time.get_ticks()
    enemy_spawn_interval = random.randint(1000,4000)
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
            now = pygame.time.get_ticks()
            # Spawn faixas periodically
            if now - last_faixa_spawn > faixa_spawn_interval:
                left = Esquerda(assets)
                right = Direita(assets)
                all_sprites.add(left, right)
                all_faixas.add(left, right)
                last_faixa_spawn = now
            # Spawn vida periodically
            if now - last_vida_spawn > vida_spawn_interval:
                vida = Vida(assets)
                all_sprites.add(vida)
                all_vidas.add(vida)
                last_vida_spawn = now
                vida_spawn_interval = random.randint(10000, 30000)
            if now - last_enemy_spawn >enemy_spawn_interval:
                enemy = Carro(assets)
                all_sprites.add(enemy)
                all_enemies.add(enemy)
                last_enemy_spawn = now
                enemy_spawn_interval = random.randint(1000,2000)
            # Enemy collisions
            hits = pygame.sprite.spritecollide(player, all_enemies, True, pygame.sprite.collide_mask)
            for hit in hits:
                print("Collision with enemy at:", hit.rect.center)
                explosao = Explosion(hit.rect.center, assets)
                all_sprites.add(explosao)
                lives -= 1
                if lives == 0:
                    explosao = Explosion(player.rect.center, assets)
                    all_sprites.add(explosao)
                    player.kill()
                    state = EXPLODING
                    explosion_tick = pygame.time.get_ticks()

            vida_hits = pygame.sprite.spritecollide(player, all_vidas, True, pygame.sprite.collide_mask)
            for vida in vida_hits:
                if lives < max_lives:
                    lives += 1

        elif state == EXPLODING:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                return DONE

        window.fill(BLACK)
        window.blit(groups['background'], (0, 0))
        all_sprites.draw(window)
        if state == PLAYING:
            window.blit(player.image, player.rect)

        for i in range(lives):
            window.blit(assets[vida2], (10 + i * 60, 10))
        all_sprites.update()
        pygame.display.update()

    return DONE