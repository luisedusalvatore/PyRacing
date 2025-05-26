import pygame
from configuracoes import *
from assets import *
clock = pygame.time.Clock()

def start(window):
    assets = load_assets()
    background_initial = assets['fundo']
    background_escolha = assets['escolha']
    font = pygame.font.SysFont(None, 48)
    title = font.render('PyRacing', True, WHITE)
    title_rect = title.get_rect(center=(WIDTH/2, HEIGHT/3))
    instructions = font.render('Press Any Key to Start', True, WHITE)
    instructions_rect = instructions.get_rect(center=(WIDTH/2, HEIGHT/2))

    running = True
    estado = 'initial'
    cor = None

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT, None
            if estado == 'initial':
                if event.type == pygame.KEYDOWN:
                    estado = 'escolha'
            elif estado == 'escolha':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        cor = 0
                        running = False
                    elif event.key == pygame.K_2:
                        cor = 1
                        running = False
                    elif event.key == pygame.K_3:
                        cor = 2
                        running = False
                    elif event.key == pygame.K_4:
                        cor = 3
                        running = False

        window.fill(BLACK)
        if estado == 'initial':
            window.blit(background_initial, (0, 0))
            window.blit(title, title_rect)
            window.blit(instructions, instructions_rect)
        elif estado == 'escolha':
            window.blit(background_escolha, (0, 0))


        pygame.display.flip()

    return GAME, cor  # Always return tuple

def game_over(window):
    assets = load_assets()
    font = assets[fonte]
    font2 = assets[fonte2]
    game_over_text = font.render("GAME OVER", True, RED)
    game_over_text2 = font2.render("Aperte qualquer tecla para voltar a jogar", True, RED)
    text_rect = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 20))
    text_rect2 = game_over_text2.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 20))
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYUP:
                return INIT
        window.fill(BLACK)
        window.blit(game_over_text, text_rect)
        window.blit(game_over_text2, text_rect2)
        pygame.display.flip()