import pygame
from configuracoes import *
import os
from classes import *
from assets import load_assets
from funcoes import *

def game_screen(window):
    assets = load_assets()
    # Relógio do sistema
    clock = pygame.time.Clock()
    background = assets[fundo]
    all_sprites = pygame.sprite.Group()
    all_enemies = pygame.sprite.Group()
    groups = {}
    groups['all_enemies'] = all_enemies
    groups['all_sprites'] = all_sprites
    groups['background'] = background


    #Criando o jogador
    player = Piloto (groups, assets)
    all_sprites.add(player)

    # Criando os carros:

    for i in range(3):
        inimigo = Carro(assets)
        all_enemies.add(inimigo)
    all_sprites.add(all_enemies)

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
                game = False
                state =  DONE
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
        
            # Verifica se houve colisão entre nave e meteoro
            hits = pygame.sprite.spritecollide(player, all_enemies, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                player.kill()
                lives -= 1
                explosao = Explosion(player.rect.center, assets)
                all_sprites.add(explosao)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosao) + 400
            elif state == EXPLODING:
                now = pygame.time.get_ticks()
                if now - explosion_tick > explosion_duration:
                    if lives == 0:
                        state = DONE
                    else:
                        state = PLAYING
                        player = Piloto(groups, assets)
                        all_sprites.add(player)
        
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(groups['background'], (0, 0))
        # atualiza a tela
        all_sprites.draw(window)
        all_sprites.update()
        pygame.display.update()